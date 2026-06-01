
# DevOps Flask App 

A simple Python Flask web application containerized with Docker and deployed using a CI/CD pipeline with GitHub Actions.

##  Tech Stack

- **Python / Flask** — Web application
- **Docker** — Containerization
- **GitHub Actions** — CI/CD Pipeline
- **Docker Hub** — Image registry

##  API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Home page |
| `/health` | Health check |
| `/info` | App version info |

##  Run Locally with Docker

```bash
docker pull YOUR_DOCKERHUB_USERNAME/devops-flask-app:latest
docker run -p 5000:5000 YOUR_DOCKERHUB_USERNAME/devops-flask-app:latest
```

Open in browser: `http://localhost:5000`

##  CI/CD Pipeline

Every push to `main` branch automatically:
1. Builds the Docker image
2. Pushes it to Docker Hub

##  Project Structure

```
devops-flask-app/
├── app.py
├── requirements.txt
├── Dockerfile
└── .github/
    └── workflows/
        └── docker.yml
```
