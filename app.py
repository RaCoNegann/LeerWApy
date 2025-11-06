from flask import Flask, request, jsonify
#import js2py
#import requests
#import json
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
        #with open("sample.txt", "w") as f:#Crei que crearia un archivo en elgithub
            #f.write("This is line 1.\n")
        # Registrar mensajes
        
        logger.debug('Este es un mensaje de depuración')
        logger.info('El programa ha comenzado con éxito')
        logger.warning('Se ha detectado una configuración no óptima')
        logger.error('Se ha producido un error al procesar los datos')
        logger.critical('El sistema ha fallado críticamente')
        
        if mode and token and mode == "subscribe" and token == VERIFY_TOKEN:
            #js_code_string = "console.log('aaaaaaaabb');"
            #result = js2py.eval_js(js_code_string)
            
            print("WEBHOOK_VERIFIED")
            return challenge, 200
        else:
            print("VERIFICATION_FAILED")
            return jsonify({"status": "error", "message": "Verification failed"}), 403

    elif request.method == "POST":
        # Handle incoming event notifications
        data = request.json
        logger.info(data)
        print("Received webhook data:", data)

        # Process the data (e.g., store in a database, send notifications)
        #url = "https://graph.facebook.com/v22.0/845427305315318/messages"
        #headers = {
        #    'Content-Type': 'application/json',
        #    'Authorization': 'Bearer EAFahY2vnTjUBP9LO96F0UYZCZCY0uCjZALa0cZBbLFiyAHsxuahw40ZCMZBYoB6t26WDA2PZCLoUASJcX1DpG7k8B0OLC1f94GfIj0qSBtiUwWO0q66GJZAPfrTVKE0ohkZA9UWvwPC6POccHthgbEpxWyPDrVnWxU1WRJb2oLwmHZB8pYHemMtbeZAVWGBaKOaiOKoYV1lQK9YfrcDwg0KMrKVZBYy1EwkZBFGumzpxjIl5iLWkkrdoibNHjU8Btp838sKx2pZAKFjSUGqEuUpjrkvRV4'
        #}
        #payload = json.dumps({
        #    "messaging_product": "whatsapp",
        #    #"to": "573202965268",
        #    "to": "573202965268",
        #    "type": "template",
        #    "template": {
        #        "name": "hello_world",
        #        "language": {
        #            "code": "en_US"
        #        }
        #    }
        #})
        #response = requests.request("POST", url, headers=headers, data=payload)
        # ...

        return jsonify({"status": "EVENT_RECEIVED"}), 200

if __name__ == "__main__":
    #app.run(debug=True, port=5000) # Run on port 5000 for local testing - Geneta como un timeout*
    app.run(host='0.0.0.0', port=5000)
