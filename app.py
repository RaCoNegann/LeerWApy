from flask import Flask, request, jsonify
import requests
import json
import logging

app = Flask(__name__)
# Obtener el logger
logger = logging.getLogger(__name__)
# Replace with your actual verify token - tal vez esto se puede hacer mejor  como en el .js
VERIFY_TOKEN = "tokenenrender"
# Configurar el logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Handle webhook verification
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        
        logger.debug('Este es un mensaje de depuración')
        #logger.info('El programa ha comenzado con éxito')
        #logger.warning('Se ha detectado una configuración no óptima')
        #logger.error('Se ha producido un error al procesar los datos')
        #logger.critical('El sistema ha fallado críticamente')
        
        if mode and token and mode == "subscribe" and token == VERIFY_TOKEN:
            print("WEBHOOK_VERIFIED")
            return challenge, 200
        else:
            print("VERIFICATION_FAILED")
            return jsonify({"status": "error", "message": "Verification failed"}), 403

    elif request.method == "POST":
        # Handle incoming event notifications
        data = request.json
        print("Received webhook data:", data)
        
        logger.warning(data)
        texto = (data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"])

        url = "https://graph.facebook.com/v22.0/845427305315318/messages"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer EAFahY2vnTjUBPygMVi10NJ7zURdbztHiSSjUSKPttPp00LqdxFVkZAddU7HOOmzYscNwwUNHcUfh20yvsfhZBbBy6C4jMG1bIpWWg5K9RIUmEzALSJlbNmMbvscs8fxjf3ERsCJju5pRig6Ae1SBbZCy5ZB20ZCAlHSgnaWNbVgskwXK1UDTWMs7pNFhE79eFDZBNXeIJN1ZA89tURZB0XwYhLMhzfZCoTF4jNHa5BPuJGpObt0HaCMm4MUqKPYGljTx0GAuuljl742cODe5yruDu'
        }
        if texto == "this is a text message":
            payload = json.dumps({
                "messaging_product": "whatsapp",
                #"to": "573202965268",
                "to": "573202965268",
                "type": "template",
                "template": {
                    "name": "hello_world",
                    "language": {
                        "code": "en_US"
                    }
                }
            })
            logger.error('Entro en el if del texto')
        else:
            payload = json.dumps({
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": "573202965268",
                "type": "text",
                "text": {
                    "preview_url": False,
                    "body": "text-message-content"
                }
            })
            logger.critical('Entro en else del texto')
        response = requests.request("POST", url, headers=headers, data=payload)
        logger.info('Deberia enviar')
        return jsonify({"status": "EVENT_RECEIVED"}), 200

if __name__ == "__main__":
    #app.run(debug=True, port=5000) # Run on port 5000 for local testing - Geneta como un timeout*
    app.run(host='0.0.0.0', port=5000)
