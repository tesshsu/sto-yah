#!/bin/bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -aG docker ec2-user
sudo yum install git -y

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone the project (replace with your repo if needed)
git clone https://github.com/your-repo/stock-app.git /home/ec2-user/stock-app

# Start the app using Docker Compose
cd /home/ec2-user/stock-app
sudo docker-compose up -d
