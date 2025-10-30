from flask import Flask, request, abort, jsonify
import os
from datetime import datetime
import json

app = Flask(__name__)

port = int(os.getenv('PORT', 10000))#No se seguro si era necesario
verify_token = os.getenv('VERIFY_TOKEN')

@app.route('/', methods=['GET'])
def verify_webhook():
    mode = request.args.get('hub.mode')
    challenge = request.args.get('hub.challenge')
    token = request.args.get('hub.verify_token')

    if mode == 'subscribe' and token == verify_token:
        print('WEBHOOK VERIFIED')
        return challenge, 200
    else:
        abort(403)

@app.route('/handle_webhook', methods=['POST'])
"""print("Sera")
print(request.get_json())"""
def handle_webhook():
    print("SeraFunc")
    print(request.get_json())
    if request.method == 'POST':
        try:
            print("SeraFunc")
            print(request.get_json())
            data = request.get_json()
            if data:
                print("Received webhook data:")
                print(jsonify(data).get_data(as_text=True))
                # Process the webhook data here (e.g., save to database, trigger other actions)
                return jsonify({"status": "success", "message": "Webhook received"}), 200
            else:
                return jsonify({"status": "error", "message": "No JSON data received"}), 400
        except Exception as e:
            return jsonify({"status": "error", "message": f"Error processing webhook: {e}"}), 500
    else:
        return jsonify({"status": "error", "message": "Method not allowed"}), 405

if __name__ == '__main__':
    print(f"\nListening on port {port}\n")
    app.run(host='0.0.0.0', port=port)
