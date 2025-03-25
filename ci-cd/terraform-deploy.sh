#!/bin/bash
# terraform-deploy.sh
# Script to apply Terraform changes for infrastructure updates.
# This script initializes Terraform, plans changes, and applies them.
# Usage: ./terraform-deploy.sh

set -e

echo "Initializing Terraform..."
cd infrastructure/terraform
terraform init

echo "Planning Terraform changes..."
terraform plan -out=tfplan.out

echo "Applying Terraform plan..."
terraform apply -auto-approve tfplan.out

echo "Terraform deployment completed successfully."
