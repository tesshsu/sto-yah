variable "aws_region" {
  description = "AWS region for the EC2 instance"
  default     = "ap-northeast-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "key_name" {
  description = "AWS Key Pair for SSH access"
  default     = "my-key"
}

variable "app_port" {
  description = "Application port"
  default     = 8000
}

variable "desired_capacity" {
  description = "Desired number of instances"
  default     = 2
}

variable "max_size" {
  description = "Maximum instances in Auto Scaling Group"
  default     = 3
}

variable "min_size" {
  description = "Minimum instances in Auto Scaling Group"
  default     = 1
}
