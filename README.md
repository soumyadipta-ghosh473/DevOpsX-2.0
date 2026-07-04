# DevOpsX-2.0

## Overview

DevOpsX 2.0 is a production-inspired DevOps project implementing a complete CI/CD pipeline using GitHub, Jenkins, Docker, Kubernetes, Terraform, Prometheus and Grafana.

---

## Features

- Flask Task Manager Application
- GitHub Source Control
- Jenkins CI/CD Pipeline
- Docker Containerization
- Kubernetes Deployment
- Infrastructure as Code using Terraform
- Monitoring using Prometheus
- Dashboard using Grafana

---

## Tech Stack

- Python Flask
- SQLite
- GitHub
- Jenkins
- Docker
- Kubernetes (Minikube)
- Terraform
- Prometheus
- Grafana
- AWS EC2 Ubuntu

---

## Architecture

Developer

↓

GitHub

↓

Jenkins

↓

Docker Build

↓

Docker Hub

↓

Kubernetes

↓

Prometheus

↓

Grafana

---

## Project Structure

```
DevOpsX-2.0
│
├── app
├── kubernetes
├── monitoring
├── terraform
├── Jenkinsfile
├── Dockerfile
└── README.md
```

---

## CI/CD Pipeline

1. Push code to GitHub

2. Jenkins detects changes

3. Build Docker image

4. Push image to Docker Hub

5. Deploy to Kubernetes

6. Monitor using Prometheus & Grafana

---

## Author

Soumyadipta Ghosh
