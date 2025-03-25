#!/bin/bash
# k8s-deploy.sh
# Script to deploy or update all services on Kubernetes.
# This script applies all Kubernetes manifests using kubectl.
# It can be used manually or triggered by CI/CD pipelines.

set -e

echo "Deploying Kubernetes resources in namespace 'prod'..."

# Apply namespace configuration
kubectl apply -f infrastructure/k8s/namespace-prod.yaml

# Deploy core microservices
kubectl apply -f infrastructure/k8s/pricing-service-deployment.yaml
kubectl apply -f infrastructure/k8s/pricing-service-service.yaml
kubectl apply -f infrastructure/k8s/forecasting-service-deployment.yaml

# Deploy front-end web portal
kubectl apply -f infrastructure/k8s/portal-deployment.yaml
kubectl apply -f infrastructure/k8s/portal-service.yaml

# Apply ingress configuration
kubectl apply -f infrastructure/k8s/ingress.yaml

# Apply ConfigMaps and Secrets
kubectl apply -f infrastructure/k8s/config-maps.yaml
kubectl apply -f infrastructure/k8s/secrets.yaml

echo "Kubernetes deployment completed successfully."
