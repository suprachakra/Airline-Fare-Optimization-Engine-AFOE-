## CI/CD Pipeline and Deployment Scripts
This folder contains the CI/CD pipeline definitions and deployment scripts for the Airline Fare Optimization Engine project. The CI/CD processes are designed to:
- Enforce a robust branching strategy (e.g., GitFlow or trunk-based development).
- Automatically build, test, and deploy services with zero manual intervention.
- Support multiple CI/CD systems (GitHub Actions, Jenkins, Azure Pipelines) and local development via Docker Compose.

### Contents
- **.github/workflows/**: GitHub Actions workflows for CI (ci.yml) and CD (cd.yml).
- **Jenkinsfile**: Jenkins pipeline for building, testing, and deploying microservices in parallel.
- **azure-pipelines.yml**: Azure Pipelines definition for building, testing, and deploying.
- **docker-compose.yml**: Docker Compose file for local development and integration testing.
- **k8s-deploy.sh**: Shell script to deploy or update all services on a Kubernetes cluster.
- **terraform-deploy.sh**: Script to apply Terraform changes as part of the deployment pipeline.

Refer to each file for detailed configuration and instructions.
