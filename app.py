from flask import Flask, request, abort
import os
from datetime import datetime
import json

app = Flask(__name__)

port = int(os.getenv('PORT', 3000))
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

@app.route('/', methods=['POST'])
def webhook():
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n\nWebhook received {timestamp}\n")
    print(json.dumps(request.json, indent=2))
    return '', 200

if __name__ == '__main__':
    print(f"\nListening on port {port}\n")
    app.run(host='0.0.0.0', port=port)
