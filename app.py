from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'succes', 200
    else:
        abort(400)

if __name__ == '--main__':
    app.rin()
