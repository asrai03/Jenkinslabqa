pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building..."'
                sh 'ls -la'
                sh 'touch buildArtifact.txt'
                sh 'echo "Build complete" > buildArtifact.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Testing..."'
                sh 'pwd'
                sh 'ls -la'
                sh 'cat buildArtifact.txt'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
                sh 'mkdir -p deploy'
                sh 'mv buildArtifact.txt deploy/'
                sh 'ls -la deploy/'
                sh 'echo "Deployment successful!"'
            }
        }
    }
}
