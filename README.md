#  DevOpsX 2.0

A production-inspired end-to-end DevOps project demonstrating Continuous Integration, Continuous Deployment (CI/CD), containerization, infrastructure automation, Kubernetes orchestration, and application monitoring on AWS.

---

#  Overview

DevOpsX 2.0 implements a complete DevOps workflow using modern cloud-native tools. The project automates application build, deployment, monitoring, and infrastructure provisioning.

---

#  Features

- Flask Task Manager Application
- REST API with Health & Metrics Endpoints
- Git Version Control using GitHub
- Automated CI/CD Pipeline using Jenkins
- Docker Containerization
- Docker Hub Image Registry
- Kubernetes Deployment using Minikube
- Infrastructure Provisioning using Terraform
- Application Monitoring using Prometheus
- Visualization using Grafana
- AWS EC2 Deployment

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Python Flask |
| Database | SQLite |
| Version Control | Git & GitHub |
| CI/CD | Jenkins |
| Containerization | Docker |
| Container Registry | Docker Hub |
| Orchestration | Kubernetes (Minikube) |
| Infrastructure as Code | Terraform |
| Monitoring | Prometheus |
| Dashboard | Grafana |
| Cloud Platform | AWS EC2 (Ubuntu) |

---

#  Architecture

```
Developer
    │
    ▼
GitHub Repository
    │
    ▼
Jenkins CI/CD
    │
    ▼
Docker Build
    │
    ▼
Docker Hub
    │
    ▼
Kubernetes (Minikube)
    │
    ├──────────────┐
    ▼              ▼
Flask App     Prometheus
                  │
                  ▼
              Grafana
```

---

# 📂 Project Structure

```
DevOpsX-2.0
│
├── app/
│   ├── templates/
│   ├── static/
│   ├── app.py
│   └── models.py
│
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
│
├── monitoring/
│   └── k8s/
│       ├── prometheus-config.yaml
│       ├── prometheus.yaml
│       └── grafana.yaml
│
├── terraform/
│   ├── main.tf
│   ├── provider.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── Dockerfile
├── Jenkinsfile
├── README.md
└── requirements.txt
```

---

# ⚙ CI/CD Workflow

1. Developer pushes code to GitHub
2. Jenkins detects repository changes
3. Docker image is built
4. Image is pushed to Docker Hub
5. Kubernetes deploys the latest image
6. Prometheus collects application metrics
7. Grafana visualizes monitoring data

---

#  Monitoring

The application exposes Prometheus metrics through:

```
/metrics
```

Health endpoint:

```
/health
```

Prometheus scrapes application metrics and Grafana provides dashboards for visualization.

---

# 🚀 Deployment Components

- AWS EC2 Ubuntu Server
- Jenkins
- Docker
- Kubernetes (Minikube)
- Prometheus
- Grafana

---

#  Screenshots

Add screenshots of:

- Jenkins Successful Pipeline
- Docker Hub Repository
- Kubernetes Pods
- Kubernetes Services
- Prometheus Targets
- Grafana Dashboard
- Terraform Apply Output
- Flask Application

---

#  Author

**Soumyadipta Ghosh**

B.Tech Computer Science Engineering

Cloud & DevOps Enthusiast
