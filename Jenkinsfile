pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                sh 'rm -rf dockerfileexercise'
                sh 'git clone https://gitlab.com/Reece-Elder/dockerfileexercise.git'
            }
        }
        stage('Build') {
            steps {
                dir('dockerfileexercise/Task1') {
                    sh 'docker build -t flask-task1 .'
                }
            }
        }
        stage('Test') {
            steps {
                sh 'docker run --rm flask-task1 python -c "print(\'App imports OK\')"'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker rm -f flask-task1-container || true'
                sh 'docker run -d -p 5500:5500 --name flask-task1-container flask-task1'
                sh 'sleep 3'
                sh 'curl http://localhost:5500'
            }
        }
    }
}
