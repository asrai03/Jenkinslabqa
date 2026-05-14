pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
                sh 'ls -la'
                sh 'docker build -t flask-task1 .'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                sh 'docker images | grep flask-task1'
                sh 'echo "Image built successfully"'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
                sh 'docker rm -f flask-task1-container || true'
                sh 'docker run -d -p 5500:5500 --name flask-task1-container flask-task1'
                sh 'sleep 3'
                sh 'curl http://localhost:5500'
                sh 'echo "Deployment successful!"'
            }
        }
    }
}
