pipeline {
  agent any

  environment {
    IMAGE_NAME = "auth-service:jenkins"
  }

  stages {
    stage('Clone Code') {
      steps {
        git 'https://github.com/imarindambaidya/cloud-native-microservices.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        dir('auth-service') {
          sh 'docker build -t $IMAGE_NAME .'
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        dir('auth-service/k8s') {
          sh 'kubectl apply -f deployment.yaml'
          sh 'kubectl apply -f service.yaml'
        }
      }
    }
  }
}