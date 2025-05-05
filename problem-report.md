# Problem Report

# This is for a Student Notification System


# Steps I took to find out what the problem was.

- I tried accessing the endpoint using the command "curl http://localhost:5001/notify"
- I verified the docker container was running " docker ps"
- I opend the app.py and found  that it was using the wrong endpoint.
- I check the status of the service "curl http://localhost:5001/status"
- I tested what is the correct endpoint "curl -X POST http://localhost:5001/send-notification -H "Content-Type: application/json" -d '{"student_id": 123, "message": "Test"}'"

# My Findings:

- The endpoint was not found for the "notify" it gave a 404 error. Which meant the web server cannot locate the specific page or resource.
- The correct endpoint is  "send-notification"
- The behavior for "send-notification" is not correct, it has radom behavior
- The server is running correctly on port 5001

  -The Random Behavior

- The /send-notification endpoint simulates various outcomes:
- "sent": normal notification
- "duplicate": indicates a repeated notification
- "skipped": mimics a failure to send
- This randomness made it difficult to test for consistent results.
  



  
  
