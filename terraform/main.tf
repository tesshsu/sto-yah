resource "aws_security_group" "app_sg" {
  name_prefix = "app-sg-"

  # Allow inbound traffic on port 8000
  ingress {
    from_port   = var.app_port
    to_port     = var.app_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow SSH access (optional, for debugging)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_launch_template" "app_template" {
  name_prefix   = "app-template-"
  image_id      = "ami-0c55b159cbfafe1f0" # Amazon Linux 2 AMI (Update with your region’s AMI)
  instance_type = var.instance_type
  key_name      = var.key_name

  user_data = base64encode(file("userdata.sh"))

  network_interfaces {
    security_groups = [aws_security_group.app_sg.id]
  }

  tag_specifications {
    resource_type = "instance"
    tags = {
      Name = "StockAppInstance"
    }
  }
}

resource "aws_autoscaling_group" "app_asg" {
  desired_capacity     = var.desired_capacity
  max_size            = var.max_size
  min_size            = var.min_size

  launch_template {
    id      = aws_launch_template.app_template.id
    version = "$Latest"
  }

  vpc_zone_identifier = ["subnet-01b56b709d4615c89", "subnet-02be83e88cb2ab9f9", "subnet-08e1ab83855946c88"]
  # Replace with your subnet IDs
}

resource "aws_lb" "app_lb" {
  name               = "app-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.app_sg.id]
  subnets           = ["subnet-01b56b709d4615c89", "subnet-02be83e88cb2ab9f9"]  # Replace with your subnet IDs
}

resource "aws_lb_target_group" "app_tg" {
  name     = "app-tg"
  port     = var.app_port
  protocol = "HTTP"
  vpc_id   = "vpc-0dbbd37ed5831e9c7"  # Replace with your VPC ID

  health_check {
    path                = "/"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }
}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.app_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.app_tg.arn
  }
}

resource "aws_autoscaling_attachment" "asg_attachment" {
  autoscaling_group_name = aws_autoscaling_group.app_asg.id
  lb_target_group_arn    = aws_lb_target_group.app_tg.arn
}
