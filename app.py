from flask import Flask, request, abort
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():
    if request.method == 'POST':
        #print(request.get_json())
        json_string = json.dumps(request.get_json())
        print(json_string)
        return 'succes', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
