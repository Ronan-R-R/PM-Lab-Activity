# TASK_PLAN.md

## Overview

This document outlines the planned execution strategy for identifying and resolving the Redis misconfiguration issue in the Dockerized Student Notification System. The root cause is hypothesized to be incorrect or missing Redis connection parameters in the notification-service configuration.

---

## Root Cause Hypothesis

The `notification-service` is unable to send messages due to incorrect Redis host/port configuration or missing Redis container linking in `docker-compose.yml`.

---

## Team Roles

| Team Member | Role Description                                                                 |
|-------------|-----------------------------------------------------------------------------------|
| Sebastian   | Tester, Collaborator, and Documenter          |
| Ronan       | Documenter, Formatter, and Repository Manager |
| Philip      | Lead Developer and Lead Tester                |
| Zandro      | Information Gatherer and Presentation Manager |

---

## Task Breakdown

| ID  | Task Description                                                  | Tool(s) Used                           | Assigned To | Priority |
|-----|-------------------------------------------------------------------|----------------------------------------|-------------|----------|
| T1  | Inspect `docker-compose.yml` for Redis service definition         | VS Code, Docker Compose                | Sebastian   | High     |     
| T2  | Verify that the Redis container is running properly               | Docker CLI (`docker ps`, `logs`)       | Ronan       | High     |     
| T3  | Examine app.py for Redis configuration variables                  | VS Code, Python                        | Sebastian   | High     |     
| T4  | Check `.env` file and environment variables                       | VS Code, Docker CLI (`exec env`)       | Zandro      | Medium   |     
| T5  | Use Redis CLI to test connection and basic commands               | Redis CLI, Docker Exec                 | Ronan       | High     |     
| T6  | Validate response from `/api/notify` endpoint                     | Postman, curl                          | Sebastian   | High     | 
| T7  | Analyze logs for stack traces or connection failures              | docker-compose logs                    | Ronan       | High     |     
| T8  | Collaboratively propose and apply Redis config fix                | VS Code, Team call                     | All Members | High     |     
| T9  | Restart all services after fix and verify with curl/Postman       | Docker CLI, Postman                    | Sebastian   | High     |     
| T10 | Document investigation results in `problem-report.md`             | VS Code                                | Philip      | Medium   |
| T11 | Finalize `problem-statement.md` based on team consensus           | VS Code                                | Philip      | Medium   |     
| T12 | Write `AGREEMENT.md` detailing root cause and agreed fix          | VS Code                                | Philip      | Medium   |     
| T13 | Update `docker-compose.yml` with correct Redis configuration      | VS Code, Docker Compose                | Zandro      | High     |     
| T14 | Submit all files via GitHub with correct commit messages          | Git, GitHub                            | Philip      | Medium   |     

---

## Timeline

| Day   | Tasks                                                                                      | Expected Output                         |
|--------|--------------------------------------------------------------------------------------------|------------------------------------------|
| Day 1 | T1, T2, T3, T4                                                                              | Initial assessment of Docker and Redis   |
| Day 2 | T5, T6, T7                                                                                  | Endpoint behavior and Redis connectivity |
| Day 3 | T8                                                                                          | Team sync + agreed solution              |
| Day 4 | T9, T13                                                                                     | Apply fix + re-run container             |
| Day 5 | T10, T11, T12, T14                                                                          | Final documentation and submission       |

---

## Collaboration & Tools

- Docker CLI: Container inspection and control
- Redis CLI: Connectivity and diagnostics
- VS Code: Editing code and Docker configurations
- Postman / curl: Endpoint testing
- Git & GitHub: Version control and collaboration
- Zoom/Discord: Team meetings for Task T8

---

## Success Criteria

- The /api/notification endpoint sends messages successfully
- Redis connection is confirmed operational via logs and CLI
- All documentation files (`problem-statement.md`, `problem-report.md`, `AGREEMENT.md`, `TASK_PLAN.md`) are completed
- Updated `docker-compose.yml` reflects correct Redis integration

---

