output "load_balancer_dns" {
  description = "DNS name of the Load Balancer"
  value       = aws_lb.app_lb.dns_name
}
