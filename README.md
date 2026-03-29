# Tummoc-devops
Python app

# TUMMOC DevOps Assignment

End-to-end DevOps pipeline built from scratch for a company with no existing DevOps practices.

## Live URLs (EC2)
- App: http://32.192.232.181:5000
- Health: http://32.192.232.181:5000/health
- Grafana: http://32.192.232.181:3000 (admin / admin123)
- Prometheus: http://32.192.232.181:9090

## What's Built

### 1. CI/CD — GitHub Actions
Pipeline triggers on every `git push` to main:
- Lint → flake8
- Test → pytest
- Build → Docker image pushed to GHCR
- Deploy → SSH into EC2, restart containers

### 2. Docker
- Multi-stage Dockerfile (builder + runtime)
- docker-compose.yml runs app + Prometheus + Grafana

### 3. Infrastructure as Code — Terraform (AWS)
- VPC, Subnet, Internet Gateway, Route Table
- EC2 t3.micro (Ubuntu 24.04)
- Security Group (ports 22, 5000, 3000, 9090)
- S3 bucket (versioned + encrypted)

### 4. Monitoring
- Prometheus scrapes /metrics every 15s
- Grafana dashboards at port 3000
- prometheus-flask-exporter auto-exposes Flask metrics

## Tech Stack
| Layer | Tool |
|-------|------|
| App | Python, Flask, Gunicorn |
| CI/CD | GitHub Actions |
| Container | Docker, Docker Compose |
| IaC | Terraform |
| Cloud | AWS (EC2, S3, VPC) |
| Monitoring | Prometheus, Grafana |


=========================================================

## 📈 Self-Assessment

| Tool / Area | Rating (1–5) | Notes |
|------------|-------------|------|
| CI/CD      | 4.3 | Built GitHub Actions pipeline |
| Docker     | 4.3 | Multi-stage build + Compose |
| Kubernetes |  4  | Basic understanding (learning) |
| Terraform  |  4  | Created infra (EC2, VPC, S3) |
| AWS/Azure  | 3.8 | Worked with EC2, networking |
| Monitoring |  3  | Prometheus + Grafana setup |
| Git        | 4.3 | Strong daily usage |

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/<your-username>/tummoc-devops.git
cd tummoc-devops

docker build -t tummoc-app .
docker run -p 5000:5000 tummoc-app

 
