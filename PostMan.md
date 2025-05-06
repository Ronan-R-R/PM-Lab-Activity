# What is Postman?
Postman is a popular API client that allows developers to test, develop, and document RESTful APIs. It provides a user-friendly interface to send requests and inspect responses without writing code or using command-line tools like curl.

# Why Do We Use Postman?
- To test APIs by sending HTTP requests (GET, POST, PUT, DELETE, etc.).
- To debug APIs and view response details such as status codes, headers, and body.
- To automate API workflows and create test scripts.
- To simulate real-world API usage during development.
- To avoid typos and malformed JSON that might happen when using the terminal.

# How Postman Works
- You create a request (e.g. a POST request to an endpoint).
- You choose the method (GET, POST, etc.).
- You enter the URL (e.g. http://localhost:5001/send-notification).
- You set the headers (e.g. Content-Type: application/json).
- You enter the request body (usually in JSON format).
- You click Send and Postman gives you:
- The response status (e.g. 200 OK or 404 Not Found).
- The response body (e.g. { "status": "sent" }).
- The headers, response time, and size.

  ============================================================

# The Problem and how I fixed it.

# Problem 1: 404 Not Found
Cause: I was using the incorrect URL endpoint in Postman:


http://localhost:5001/notify
Why: I assumed /notify was a valid route.
Fix: I checked the app.py code and saw the correct endpoint was:
http://localhost:5001/send-notification

What I did:
Updated the request URL in Postman to /send-notification.
Retested the request.

# Problem 2: Random Behavior in Responses

Cause: The /send-notification endpoint randomly returned sent, skipped, or duplicate.
Why it was a problem: I needed consistent, predictable test results in Postman.
Fix:
Modified the code to support a query parameter: ?disable_random=true
Then used this URL in Postman:
http://localhost:5001/send-notification?disable_random=true
Result: The response became consistent with:


{
  "status": "sent",
  "student_id": 123,
  "message": "Test notification"
}

# Problem 3: Incorrect Headers

Cause: I initially forgot to set the Content-Type: application/json header in Postman.
Why it matters: The server expects JSON input. Without this header, it couldn’t parse the request.
Fix:
In Postman, went to the Headers tab.
Added:
Key: Content-Type
Value: application/json

# Problem 4: Missing Request Body
Cause: I didn’t enter a request body or used incorrect formatting.

Fix:
Went to Body > raw > JSON in Postman.
Entered:


{
  "student_id": 123,
  "message": "Test notification"
}

# Final Testing Setup in Postman

Method: POST

URL:http://localhost:5001/send-notification?disable_random=true

Headers:

pgsql
Content-Type: application/json
Body (raw > JSON):



{
  "student_id": 123,
  "message": "Test notification"
}

The Output:

{
  "status": "sent",
  "student_id": 123,
  "message": "Test notification"
}
