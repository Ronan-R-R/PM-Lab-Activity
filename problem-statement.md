# problem-statement.md

This document outlines the unified and refined problem statement for the PM Lab Activity project after collaborative investigation and stakeholder feedback.

---

## Summary

The Student Notification System, specifically the `notification-service`, is not functioning as intended. When a request is made to notify students, the expected outcome (an email notification) is not achieved.

---

## Observed Behavior

- API requests to the `notification-service` return success or no errors, but **no actual notifications are sent**.
- Logs from the `notification-service` show failure or absence of Redis connection attempts.
- Redis appears to be running but is **not receiving any publish-subscribe messages** from the service.

---

## Replication Steps

1. Start the system using `docker-compose up`.
2. Send a test request to the `notification-service` using Postman or `curl`.
3. Observe that no Redis messages are published, and no emails are sent.
4. Review logs using `docker logs notification-service` and confirm the missing or failed Redis interaction.

---

## Defined Problem

> The `notification-service` in the Dockerized Student Notification System fails to deliver student email notifications due to a **misconfiguration or communication failure with the Redis broker**.

---

## Impact

- Students are not receiving important email updates from the system.
- System reliability and expected service behavior are compromised.
- Could cause user trust issues if not resolved promptly.

---

## Stakeholder Feedback

Stakeholders have confirmed that the issue lies in the Redis configuration or internal Docker network communication. They emphasized the importance of fixing this issue without introducing downtime or changing the external API contract.

---

This problem statement serves as the foundation for defining the resolution plan outlined in `AGREEMENT.md` and `TASK_PLAN.md`.
