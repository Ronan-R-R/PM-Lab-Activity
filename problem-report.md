
# Problem Report: Dockerized Student Notification System

## Objective

To define and document issues in a Dockerized microservice-based student notification system, and propose potential solutions based on findings during the lab activity.

---

## Issues Found

### 1. 404 Error on `/api/notify` Endpoint

**Symptom**  
When testing the `/api/notify` endpoint using:  
```bash
curl http://localhost:5001/api/notify
```
a `404 Not Found` error is returned.

**Potential Solutions**
- **Check Flask Route Definition**  
  Ensure that the `/api/notify` route is properly defined in `app.py` and correctly mapped to the desired functionality.
- **Verify Docker Container Setup**  
  Enter the container and confirm that the latest version of the application is running with the correct route mappings.
- **Inspect Flask Logs**  
  Check Flask logs inside the container for any application startup issues or route registration errors.

---

### 2. Obsolete `version` Attribute in `docker-compose.yml`

**Symptom**  
The following warning appeared in the Docker logs:  
`The attribute 'version' is obsolete.`

**Potential Solutions**
- **Remove `version` Field**  
  The `version` field is no longer required in newer Docker Compose versions. Removing it will resolve the warning and improve compatibility.
- **Update `docker-compose.yml`**  
  Ensure the Compose file syntax aligns with the latest Docker Compose standards.

---

### 3. Missing Response from Notification API

**Symptom**  
The notification service is running, but there is no response or action performed when accessing the `/api/notify` endpoint.

**Potential Solutions**
- **Confirm API Logic**  
  Review the application code to ensure the logic for sending notifications is implemented and correctly tied to the `/api/notify` endpoint.
- **Test Locally in Development**  
  Run the application outside of Docker to determine if the issue is container-related or exists in the core application logic.

---

## Task-Based Diagnostic Report

### 🚫 What’s Going Wrong?

The notification-service is not responding as expected when requests are sent to the `/api/notify` route. Instead of handling the request, the system returns a 404 error, indicating the endpoint can’t be found.

### ⏱️ When Does the Error Occur?

The failure occurs consistently on each attempt to access the notification endpoint, including through tools like curl and Postman.

### ❗ Observed Behavior

Despite the Flask server successfully starting (as shown in the logs), there is no indication that the `/api/notify` route has been registered or is available.

### 🔍 Suspected Causes

#### Likely Explanations
- The route `/api/notify` may not actually exist within the Flask app (`app.py`).
- There might be a typo in the Flask route or in the request URL being used.
- The Flask app could be running without successfully loading the function tied to the route.

#### Rare but Possible Explanations

1. **📛 Route Path Is Incorrectly Defined**  
   The route may have been written without a leading slash (e.g., `@app.route('api/notify')`).

2. **📦 Missing Blueprint Registration**  
   If routes are defined using a Flask Blueprint, it may not have been registered with the app using `app.register_blueprint(...)`.

3. **📨 Method Restriction**  
   If the route only allows POST, sending a GET request will trigger a 404 instead of a 405 error.  
   Try:  
   ```bash
   curl -X POST http://localhost:5001/api/notify
   ```

4. **🐳 Docker Cache Issues**  
   Docker might be using an outdated image that lacks the new route.  
   Use this to rebuild:  
   ```bash
   docker-compose build --no-cache
   ```

5. **🗂️ File Not Included in Image**  
   The Dockerfile or `.dockerignore` might be set up in a way that excludes `app.py`, preventing route registration.

6. **🧠 Route Only Defined in Main Block**  
   If the route is declared inside `if __name__ == "__main__":`, it won’t load properly when run in Docker or other non-interactive environments.

7. **📂 Wrong Working Directory**  
   Docker may be running the Flask app from a location where it cannot access `app.py` or related code.

8. **`/` or No `/`? Trailing Slash Issues**  
   Accessing `/api/notify` vs. `/api/notify/` may matter. Flask may return 404 if the trailing slash doesn’t match the route definition.

9. **🚫 Import Failures**  
   If your routes are split across multiple files and one fails to import silently, the route registration will also fail.

10. **🧙 Invisible Characters**  
    Sometimes copy-paste introduces hidden characters in strings. These can make routes fail to register correctly even though they look fine.

---

## Conclusion

The student notification service encountered several issues:

- A 404 error on the `/api/notify` endpoint, likely due to improper Flask route setup.
- A deprecated `version` attribute in the `docker-compose.yml` file.
- Lack of response from the notification API due to possibly unlinked backend logic.

**Recommended actions** include:
- Verifying route definitions and Flask logs.
- Updating the Compose file to remove deprecated elements.
- Testing the application both inside and outside of Docker containers for accurate diagnosis and resolution.

---