import json
import EnviarMensaje
import logging

def validar_mensaje(texto,numeroUsuario):
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
    elif "oli" in texto or "oli" in texto:
        recipient_type = "individual"
        typeAPIWA ="text"
        typeJSONAPIWA = json.dumps({
            "preview_url": False,
            "body": "Cual 'oli'\n*Madure*"
        })
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
