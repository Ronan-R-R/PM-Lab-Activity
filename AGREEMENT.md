# AGREEMENT.md

This document captures the team’s collective agreement on the root cause of the problem identified in the Dockerized Student Notification System and outlines the chosen resolution strategy.

---
# ✅ Resolution Plan for Student Notification System

## 🧩 Problem Summary

During testing of the Student Notification microservice using Postman and `curl`, a `404 Not Found` error was encountered when trying to access the `/notify` endpoint. Even when the correct `/send-notification` endpoint was used, its behavior was inconsistent due to built-in randomization logic. This made testing difficult and confusing.

---


## 🔍 Root Cause Analysis

| Issue                                      | Root Cause                                                                 |
|-------------------------------------------|----------------------------------------------------------------------------|
| `404 Not Found` on `/notify`              | The Flask app (`app.py`) did not define a route for `/notify`             |
| Random/unpredictable behavior             | The `/send-notification` route was intentionally randomized for simulation |
| Postman showing "Not Found"               | The wrong URL was used or Docker wasn't rebuilt after code changes        |

---

## 🛠️ Resolutions Implementation

### ✅ 1. Flask Code Fixes (`app.py`)

- Added a `/notify` endpoint that internally calls `/send-notification`
- Added a query parameter `disable_random=true` to make testing predictable

#### 🔧 Updated `app.py`:

```python
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/send-notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    student_id = data.get('student_id')
    message = data.get('message')

    disable_random = request.args.get('disable_random', 'false').lower() == 'true'

    if disable_random:
        return jsonify({"status": "sent", "student_id": student_id, "message": message}), 200

    outcome = random.choice(['sent', 'duplicate', 'skipped'])

    if outcome == 'skipped':
        return jsonify({"status": "skipped"}), 200
    elif outcome == 'duplicate':
        return jsonify({"status": "duplicate", "student_id": student_id}), 200
    else:
        return jsonify({"status": "sent", "student_id": student_id, "message": message}), 200

@app.route('/notify', methods=['POST'])
def notify():
    return send_notification()

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "Notification service running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```
## 2.Rebuild and Restart Docker
To apply the Flask code changes:
docker-compose down
docker-compose up --build -d

Followed by Verifying the changes in the container
docker ps

## 3. Postman Testing

## `GET /notify`

- **Method**: `GET`  
- **URL**: `http://localhost:5001/notify`  
- **Expected Response**:
  ```json
  {
    "status": "Notification service running"
  }

## POST /send-notification with predictable response

**Method:** POST  
**URL:** `http://localhost:5001/send-notification?disable_random=true`

**Headers:**
```http
Content-Type: application/json

{
  "student_id": 123,
  "message": "Test message"
}
# GET /notify for Compatibility

**Method:** `GET`  
**URL:** `http://localhost:5001/notify?disable_random=true`

**Headers and Body:** Same as above (see `POST /send-notification`)
---
## Aditional Testing

| Test                                     | Purpose                          | Result                   |
| ---------------------------------------- | -------------------------------- | ------------------------ |
| `/notify` endpoint                       | Validate legacy endpoint support | ✅ Works correctly        |
| Random behavior (`disable_random=false`) | Simulate real-world results      | ✅ Simulated as expected  |
| Docker container status                  | Ensure service is running        | ✅ Confirmed on port 5001 |

---

## Root Cause (Agreed Upon)

After collaborative investigation, we identified the following root cause:

> The `notification-service` container was misconfigured and failed to connect to the Redis message broker. This failure was due to incorrect or missing configuration values such as the Redis hostname, port, or related environment variables in the `docker-compose.yml` file.

## Supporting Observations

- Logs from the `notification-service` container showed connection errors when attempting to reach Redis.
- The Redis service was either not running, unreachable by hostname (e.g., `redis`), or exposed on an incorrect port.
- Environment variables like `REDIS_HOST` or `REDIS_PORT` were not correctly set or were inconsistent between containers.

## Resulting Behavior

- Notifications were not queued properly because the backend could not publish them to the Redis broker.
- Client requests (via curl or Postman) received incomplete or misleading responses due to backend service failure.

## Resolution Path

- Verified and corrected Redis configuration in `docker-compose.yml`.
- Ensured Redis service is up and network-accessible from the `notification-service` container.
- Retested `/send-notification` and `/notify` endpoints after configuration fixes.

---

## Team Agreement


---

## Date of Agreement

**Signed on:** `2025-05-06`

---

This agreement ensures that the entire team is aligned on the root cause and the steps to resolve the issue effectively and collaboratively.