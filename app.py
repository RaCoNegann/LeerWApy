from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_webhook():
    if request.method == 'POST':
        try:
            # Get the JSON data from the request body
            data = request.get_json()
            if data is None:
                return jsonify({"message": "Invalid JSON payload"}), 400

            print(f"Received webhook payload: {data}")
            # Process the webhook data here
            return jsonify({"message": "Webhook received successfully"}), 200

        except Exception as e:
            print(f"Error processing webhook: {e}")
            return jsonify({"message": f"Error processing webhook: {e}"}), 500
    else:
        return jsonify({"message": "Method not allowed"}), 405

if __name__ == '__main__':
    # Run the Flask app on a specific port (e.g., 5000)
    app.run(debug=True, port=5000)
