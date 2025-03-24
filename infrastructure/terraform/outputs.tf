# outputs.tf
# Terraform output values to be used by deployment pipelines and other systems.

output "vpc_id" {
  description = "The ID of the VPC created."
  value       = aws_vpc.main_vpc.id
}

output "public_subnet_id" {
  description = "The ID of the public subnet."
  value       = aws_subnet.public_subnet.id
}

output "eks_cluster_endpoint" {
  description = "The endpoint URL for the EKS cluster."
  value       = module.eks.cluster_endpoint
}

output "ecr_repository_url" {
  description = "URL of the created ECR repository."
  value       = aws_ecr_repository.dfae_repository.repository_url
}
