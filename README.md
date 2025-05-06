
# PM Lab Activity – Dockerized Student Notification System

This repository documents a lab project aimed at identifying, analyzing, and resolving a problem in a Dockerized microservice-based **Student Notification System**. The project emphasizes teamwork, communication, and structured planning in a DevOps setting using tools like Docker, Visual Studio Code, and GitHub.

## Lab Objective

To simulate a real-world development environment where a team must:

- Define a technical problem in a containerized system.
- Communicate findings to stakeholders.
- Collaborate to propose and plan a resolution.
- Document tasks, responsibilities, and timelines.

## Lab Setup

### Prerequisites

- Visual Studio Code with Docker extension  
- Docker & Docker Compose installed  
- Internet access (to pull images)  
- Project files (`docker-compose.yml`, microservices)

### Steps

```bash
# Clone the original notification system repository
git clone https://github.com/instructor/student-notification-system.git
cd student-notification-system

# Open the project in VS Code and inspect Docker setup
code .

# Start the system
docker-compose up -d

# Check running containers and logs
docker ps
docker-compose logs notification-service
```

## Lab Activities & Deliverables

### Task 1: Define the Problem (PA0101 / IAC0101)

- Examine logs and API behavior.
- Test with tools like `curl` or Postman.
- Document findings in `problem-report.md`.

### Task 2: Stakeholder Discussion (PA0102 / IAC0102)

- Present `problem-report.md` in Markdown Preview.
- Collect stakeholder feedback.
- Update the report accordingly.

### Task 3: Team Review (PA0103 / IAC0103)

- Collaborate in teams.
- Merge reports into `problem-statement.md`.

### Task 4: Document Agreement (PA0104 / IAC0104)

- Agree on root cause, tools, and roles.
- Record in `AGREEMENT.md`.

### Task 5: Plan Execution (PA0105 / IAC0105)

- Define tasks, assign team members.
- Document in `TASK_PLAN.md`.

## Presentation Guidelines

Each team prepares a presentation (10+ slides, 8–15 mins) covering:

1. Problem Overview
2. Evidence & Symptoms
3. Stakeholder Feedback
4. Final Problem Definition
5. Task Execution Plan
6. Team Reflections

## Project Structure

```
├── problem-report.md
├── problem-statement.md
├── AGREEMENT.md
├── TASK_PLAN.md
├── docker-compose.yml
└── README.md
```

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [VS Code Docker Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)