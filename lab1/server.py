from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/api/data', methods=['GET', 'POST'])
def receive_data():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        if data is None:
            return jsonify({"error": "Request body must be valid JSON"}), 400
        print("Received data:", data)
        return jsonify({"message": "Data received successfully!"}), 200
    else:
        return jsonify({"message": "This endpoint accepts POST requests to receive data."}), 200