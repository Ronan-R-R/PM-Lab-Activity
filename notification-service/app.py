from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/send-notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    student_id = data.get('student_id')
    message = data.get('message')

    # Check if random behavior is disabled
    disable_random = request.args.get('disable_random', 'false').lower() == 'true'

    if disable_random:
        # Always return a successful "sent" response
        return jsonify({
            "status": "sent",
            "student_id": student_id,
            "message": message
        }), 200

    # Simulate random response: success, duplicate, or skip
    outcome = random.choice(['sent', 'duplicate', 'skipped'])

    if outcome == 'skipped':
        return jsonify({"status": "skipped"}), 200
    elif outcome == 'duplicate':
        return jsonify({
            "status": "duplicate",
            "student_id": student_id
        }), 200
    else:
        return jsonify({
            "status": "sent",
            "student_id": student_id,
            "message": message
        }), 200

@app.route('/notify', methods=['POST'])
def notify():
    # Redirect /notify to the main send-notification handler
    return send_notification()

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Notification service running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
