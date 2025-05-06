# Postman Test Guide

This guide outlines how to test the Student Notification System using Postman.

---

## Prerequisites

Ensure the following before proceeding:

- Docker and Docker Compose are installed and running.
- The application services are up and running via Docker Compose.
- Postman is installed on your system.

---

## Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ronan-R-R/PM-Lab-Activity.git
   cd PM-Lab-Activity
   ```

2. **Start the Services**

   ```bash
   docker-compose up -d
   ```

   This command will start all the necessary services in detached mode.

3. **Verify Service Status**

   Ensure all services are running:

   ```bash
   docker ps
   ```

   You should see containers for `notification-service`, `redis`, and any other relevant services.

---

## Testing with Postman

1. **Import the Postman Collection**

   - Open Postman.
   - Click on **Import**.
   - Select the `postman_collection.json` file located in the project root directory.

2. **Configure the Environment (If Applicable)**

   - Set up any required environment variables, such as `{{base_url}}`, to point to your local services.

3. **Send a Test Notification**

   - In the imported collection, locate the **Send Notification** request.
   - Click **Send** to dispatch a test notification.

4. **Verify the Response**

   - A successful response should return a status code `200 OK`.
   - The response body should confirm that the notification was sent.

5. **Check Redis for Messages**

   - Access the Redis CLI:

     ```bash
     docker exec -it <redis_container_name> redis-cli
     ```

   - Verify that the message was published to the appropriate channel.

---

## Troubleshooting

- **No Response or Errors**

  - Check if the `notification-service` container is running:

    ```bash
    docker ps
    ```

  - Review logs for any errors:

    ```bash
    docker logs notification-service
    ```

- **Redis Connection Issues**

  - Ensure that the `notification-service` is correctly configured to connect to Redis.
  - Verify Redis is running and accessible.

- **Postman Environment Variables**

  - Confirm that all necessary environment variables in Postman are correctly set.

---

## Conclusion

By following this guide, you should be able to test the notification functionality of the Student Notification System using Postman. Ensure all services are running correctly and that Postman is properly configured to interact with them.

---