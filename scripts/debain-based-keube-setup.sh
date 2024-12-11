#!/bin/bash

echo "Updating system packages..."
sudo apt-get update
sudo apt-get upgrade

echo "Installing docker from snap store..."
sudo snap install docker

echo "Installing docker service file..."
sudo apt install docker.io

echo "Ensuring docker service in enabled..."
sudo systemctl daemon-reload
sudo systemctl enable docker
sudo systemctl start docker

echo "Installing kubernates local cluster management tool..."
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

echo "Installing kubectl..."
sudo snap install kubectl --classic

echo "Installation summary:"
docker --version
minikube version
kubectl version --client
