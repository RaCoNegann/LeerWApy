import requests
import json
import os
import MensajeDebug as mensajeDebug

def enviar_mensaje(payload):
    url = "https://graph.facebook.com/v22.0/845427305315318/messages"
    tokenApiWA = obtenerToke()
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+tokenApiWA
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    del tokenApiWA
    mensajeDebug.mensajeConsola("EnviarMensaje",response.text,1)

def enviar_imagen(numeroUsuario):
    url = "https://graph.facebook.com/v22.0/845427305315318/media"
    payload = {'messaging_product': 'whatsapp'}
    files=[
    ('file',('i_grafico.png',open("i_grafico"+numeroUsuario+".png",'rb'),'image/png'))
    ]
    tokenApiWA = obtenerToke()
    headers = {
    'Authorization': 'Bearer '+tokenApiWA
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    id=response.text.split('"')
    mensajeDebug.mensajeConsola("EnviarMensaje",id[3],2)
    #print(id[3])
    # directorio_actual = os.getcwd()
    # ruta_imagen = directorio_actual+"\\"+"i_grafico"+numeroUsuario+".png"
    # print(ruta_imagen)
    # os.remove(ruta_imagen)
    url2 = "https://graph.facebook.com/v22.0/845427305315318/messages"
    payload2 = json.dumps({
    "messaging_product": "whatsapp",
    "recipient_type": "individual",
    "to": numeroUsuario,
    "type": "image",
    "image": {
        "id": id[3]
        }
    })
    headers2 = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+tokenApiWA
    }
    response2 = requests.request("POST", url2, headers=headers2, data=payload2)
    mensajeDebug.mensajeConsola("EnviarMensaje",response2.text,2)

def obtenerToke():
    with open('tokenAPIWA.txt', 'r') as archivoToken:
        try:
            tokenApiWA = archivoToken.read()
            #if "\n" in tokenApiWA:
            tokenApiWA = tokenApiWA.strip()
            mensajeDebug.mensajeConsola("EnviarMensaje",tokenApiWA + " - to\nken",1)
        finally:
            archivoToken.close()
    return tokenApiWA