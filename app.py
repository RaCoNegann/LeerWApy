from flask import Flask, request, jsonify
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
            logger.debug('WEBHOOK_VERIFIED')
            return challenge, 200
        else:
            logger.error('VERIFICATION_FAILED')
            return jsonify({"status": "error", "message": "Verification failed"}), 403
    elif request.method == "POST":
        # Handle incoming event notifications
        data = request.json
        #print("Received webhook data:", data)
        logger.warning(data)
        try:
            texto = (data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"])
            numeroUsuario= data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
            LeerMensaje.validar_mensaje(texto,numeroUsuario)
        except:
            logger.error("No es mensaje de usuario")
        logger.info('Deberia enviar')
        return jsonify({"status": "EVENT_RECEIVED"}), 200

if __name__ == "__main__":
    #app.run(debug=True, port=5000) # Run on port 5000 for local testing - Geneta como un timeout*
    app.run(host='0.0.0.0', port=5000)
