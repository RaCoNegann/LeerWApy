import requests
import logging

def enviar_mensaje(payload):
    logger = logging.getLogger(__name__)
    url = "https://graph.facebook.com/v22.0/845427305315318/messages"
    with open('tokenAPIWA.txt', 'r') as archivo:
        try:
            tokenApiWA = archivo.read()
            tokenApiWA = tokenApiWA[:-1]
            logger.info(tokenApiWA + " - to\nken")
            #print((tokenApiWA))
        finally:
            archivo.close()
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+tokenApiWA
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    del tokenApiWA
    logger.warning(response.text)

def enviar_imagen(numeroUsuario):
    url = "https://graph.facebook.com/v22.0/845427305315318/media"
    payload = {'messaging_product': 'whatsapp'}
    files=[
    ('file',('i_grafico.png',open("i_grafico"+numeroUsuario+".png",'rb'),'image/png'))
    ]
    with open('tokenAPIWA.txt', 'r') as archivo:
        try:
            tokenApiWA = archivo.read()
            tokenApiWA = tokenApiWA[:-1]
            logger.info(tokenApiWA + " - to\nken")
        finally:
            archivo.close()
    headers = {
    'Authorization': 'Bearer '+tokenApiWA
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    id=response.text.split('"')
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
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+tokenApiWA
    }
    response2 = requests.request("POST", url2, headers=headers, data=payload2)
    logger.warning(response2.text)
