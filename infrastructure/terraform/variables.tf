# variables.tf
# Terraform input variables for configuring the infrastructure.

variable "aws_region" {
  description = "AWS region to deploy resources in."
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC."
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for the public subnet."
  type        = string
  default     = "10.0.1.0/24"
}

variable "private_subnet_cidr" {
  description = "CIDR block for the private subnet."
  type        = string
  default     = "10.0.2.0/24"
}

variable "public_az" {
  description = "Availability zone for public subnet."
  type        = string
  default     = "us-east-1a"
}

variable "private_az" {
  description = "Availability zone for private subnet."
  type        = string
  default     = "us-east-1b"
}

variable "cluster_name" {
  description = "EKS cluster name."
  type        = string
  default     = "dfae-cluster"
}

variable "node_desired_capacity" {
  description = "Desired number of worker nodes."
  type        = number
  default     = 3
}

variable "node_max_capacity" {
  description = "Maximum number of worker nodes."
  type        = number
  default     = 5
}

variable "node_min_capacity" {
  description = "Minimum number of worker nodes."
  type        = number
  default     = 1
}

variable "node_instance_type" {
  description = "EC2 instance type for EKS worker nodes."
  type        = string
  default     = "t3.medium"
}

variable "lb_security_group" {
  description = "Security group ID for the load balancer."
  type        = string
  default     = "sg-0123456789abcdef0"
}
