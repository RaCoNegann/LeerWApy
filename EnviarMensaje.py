import requests
import logging

def enviar_mensaje(payload):
    logger = logging.getLogger(__name__)
    url = "https://graph.facebook.com/v22.0/845427305315318/messages"
    with open('tokenAPIWA.txt', 'r') as archivo:
        try:
            tokenApiWA = archivo.read()
            tokenApiWA2 = tokenApiWA[:-2]
            logger.info(tokenApiWA2 + " - to\nken")
        finally:
            archivo.close()
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+tokenApiWA2
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    del tokenApiWA
    logger.warning(response.text)
