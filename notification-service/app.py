
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/send-notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    student_id = data.get('student_id')
    message = data.get('message')

    # Simulated bug: randomly skip or duplicate
    outcome = random.choice(['success', 'duplicate', 'skip'])

    if outcome == 'skip':
        return jsonify({"status": "skipped"}), 200
    elif outcome == 'duplicate':
        return jsonify({"status": "duplicate", "student_id": student_id}), 200
    else:
        return jsonify({"status": "sent", "student_id": student_id, "message": message}), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Notification service running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
