#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "=========================================="
echo " Updating System Packages..."
echo "=========================================="
sudo apt-get update && sudo apt-get upgrade -y

echo "=========================================="
echo " Installing Docker & Docker Compose Plugin..."
echo "=========================================="
# Downloads and runs the official Docker convenience script
curl -fsSL https://docker.com -o get-docker.sh
sudo sh get-docker.sh

# Remove the temporary setup script
rm get-docker.sh

echo "=========================================="
echo " Configuring User Permissions..."
echo "=========================================="
# Adds the current user to the docker group so you can run docker without sudo
sudo usermod -aG docker $USER

echo "=========================================="
echo " Verification"
echo "=========================================="
echo "Docker Version: $(docker --version)"
echo "Docker Compose Version: $(docker compose version)"

echo "------------------------------------------"
echo " SUCCESS! Installation complete."
echo " IMPORTANT: Please log out and log back in (or run 'newgrp docker') for the Docker group changes to take effect."
echo "=========================================="
