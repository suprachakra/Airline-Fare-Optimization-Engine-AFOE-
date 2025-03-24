# services.tf
# Terraform configuration for deploying additional services and resources,
# such as container registries, load balancers, and IAM roles.

# Example: Create an ECR repository for container images.
resource "aws_ecr_repository" "dfae_repository" {
  name = "airline-fare-optimization-engine"
  image_tag_mutability = "MUTABLE"
  lifecycle_policy {
    policy = <<EOF
{
  "rules": [
    {
      "rulePriority": 1,
      "description": "Expire untagged images older than 30 days",
      "selection": {
        "tagStatus": "untagged",
        "countType": "sinceImagePushed",
        "countUnit": "days",
        "countNumber": 30
      },
      "action": {
        "type": "expire"
      }
    }
  ]
}
EOF
  }
}

# Example: Create an Application Load Balancer for the web portal.
resource "aws_lb" "app_lb" {
  name               = "app-lb"
  internal           = false
  load_balancer_type = "application"
  subnets            = [aws_subnet.public_subnet.id]
  security_groups    = [var.lb_security_group]

  tags = {
    Name = "app-lb"
  }
}
