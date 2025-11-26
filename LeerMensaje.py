import json
import EnviarMensaje
import logging
import Grafica

def validar_mensaje(texto,numeroUsuario):
    aux = False
    logger = logging.getLogger(__name__)
    logger.info("Entra funcion")
    if texto == "this is a text message":
        typeAPIWA ="template"
        typeJSONAPIWA = json.dumps({
            "name": "hello_world",
            "language": {
                "code": "en_US"
            }
        })
    elif "oli" in texto or "Oli" in texto:
        recipient_type = "individual"
        typeAPIWA ="text"
        typeJSONAPIWA = json.dumps({
            "preview_url": False,
            "body": "Cual 'oli'\n*Madure*"
        })
    elif "gasto" in texto or "Gasto" in texto:
        logger.info("gasto")
        Grafica.guardar_dato(texto,numeroUsuario,False)
        aux = True
    elif "Llenar" in texto or "llenar" in texto:
        print("llenar")
        Grafica.guardar_dato(texto,numeroUsuario,True)
        aux = True
    elif texto == "graf":
        logger.info("grafica")
        Grafica.grafica(numeroUsuario)
        EnviarMensaje.enviar_imagen(numeroUsuario)
        aux = True
    else:
        recipient_type = "individual"
        typeAPIWA ="text"
        typeJSONAPIWA = json.dumps({
            "preview_url": False,
            "body": "text-message-content\nSaltoLinea"
        })
        logger.info("Valida mensaje")

    if 'recipient_type' in locals():
        payload = json.dumps({
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": numeroUsuario,
            "type": typeAPIWA,
            typeAPIWA: typeJSONAPIWA
        })
        EnviarMensaje.enviar_mensaje(payload)
    elif aux:
        aux = False
    else:
        payload = json.dumps({
            "messaging_product": "whatsapp",
            #"to": "573202965268",
            "to": numeroUsuario,
            "type": typeAPIWA,
            typeAPIWA: typeJSONAPIWA
        })
        EnviarMensaje.enviar_mensaje(payload)
    del numeroUsuario
