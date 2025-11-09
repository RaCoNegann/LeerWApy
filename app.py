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
        #logger.info('El programa ha comenzado con éxito')
        #logger.warning('Se ha detectado una configuración no óptima')
        #logger.error('Se ha producido un error al procesar los datos')
        #logger.critical('El sistema ha fallado críticamente')
        if mode and token and mode == "subscribe" and token == VERIFY_TOKEN:
            print("WEBHOOK_VERIFIED")
            logger.debug('WEBHOOK_VERIFIED')
            return challenge, 200
        else:
            #print("VERIFICATION_FAILED")
            logger.error('VERIFICATION_FAILED')
            return jsonify({"status": "error", "message": "Verification failed"}), 403

    elif request.method == "POST":
        # Handle incoming event notifications
        data = request.json
        #print("Received webhook data:", data)
        logger.warning(data)
        texto = (data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"])
        numeroUsuario= data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
        enviar_mensaje(texto,numeroUsuario)
        logger.info('Deberia enviar')
        return jsonify({"status": "EVENT_RECEIVED"}), 200
    
def enviar_mensaje(f_texto,f_cel):
    url = "https://graph.facebook.com/v22.0/845427305315318/messages"
    with open('tokenAPIWA.txt', 'r') as archivo:
        try:
            tokenApiWA = archivo.read()
            #print(type(tokenApiWA))
        finally:
            archivo.close()
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+tokenApiWA
    }
    if f_texto == "this is a text message":
        typeAPIWA ="template"
        typeJSONAPIWA = json.dumps({
            "name": "hello_world",
            "language": {
                "code": "en_US"
                }
            })
    elif "oli" in f_texto or "oli" in f_texto:
        recipient_type = "individual"
        typeAPIWA ="text"
        typeJSONAPIWA = json.dumps({
            "preview_url": False,
            "body": "Cual 'oli'\n*Madure*"})
    else:
        recipient_type = "individual"
        typeAPIWA ="text"
        typeJSONAPIWA = json.dumps({
            "preview_url": False,
            "body": "text-message-content\nSaltoLinea"})
        
    if 'recipient_type' in locals():
        payload = json.dumps({
            "messaging_product": "whatsapp",
            "recipient_type": recipient_type,
            "to": f_cel,
            "type": typeAPIWA,
            typeAPIWA: typeJSONAPIWA
        })
    else:
        payload = json.dumps({
            "messaging_product": "whatsapp",
            #"to": "573202965268",
            "to": f_cel,
            "type": typeAPIWA,
            typeAPIWA: typeJSONAPIWA
            })
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    del f_cel, tokenApiWA


if __name__ == "__main__":
    #app.run(debug=True, port=5000) # Run on port 5000 for local testing - Geneta como un timeout*
    app.run(host='0.0.0.0', port=5000)
