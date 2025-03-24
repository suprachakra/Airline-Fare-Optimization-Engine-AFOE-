# main.tf
# Main Terraform configuration to provision core infrastructure.

provider "aws" {
  region = var.aws_region
}

# VPC configuration
resource "aws_vpc" "main_vpc" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "main-vpc"
  }
}

# Subnet configuration (example for two subnets)
resource "aws_subnet" "public_subnet" {
  vpc_id            = aws_vpc.main_vpc.id
  cidr_block        = var.public_subnet_cidr
  availability_zone = var.public_az
  tags = {
    Name = "public-subnet"
  }
}

resource "aws_subnet" "private_subnet" {
  vpc_id            = aws_vpc.main_vpc.id
  cidr_block        = var.private_subnet_cidr
  availability_zone = var.private_az
  tags = {
    Name = "private-subnet"
  }
}

# EKS Cluster (Kubernetes cluster)
module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = var.cluster_name
  cluster_version = "1.21"
  subnets         = [aws_subnet.public_subnet.id, aws_subnet.private_subnet.id]
  vpc_id          = aws_vpc.main_vpc.id

  node_groups = {
    eks_nodes = {
      desired_capacity = var.node_desired_capacity
      max_capacity     = var.node_max_capacity
      min_capacity     = var.node_min_capacity
      instance_type    = var.node_instance_type
    }
  }
}
