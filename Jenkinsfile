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
        stage('Filesystem Scan') {
            steps {
                sh 'echo "Running Trivy filesystem scan..."'
                sh 'trivy fs -f json -o fs-scan-results.json .'
                archiveArtifacts artifacts: 'fs-scan-results.json', fingerprint: true
            }
        }
        stage('Image Scan') {
            steps {
                sh 'echo "Running Trivy image scan..."'
                sh 'trivy image --severity HIGH,CRITICAL -f json -o image-scan-results.json flask-task1'
                archiveArtifacts artifacts: 'image-scan-results.json', fingerprint: true
            }
        }
        stage('Security Gate') {
            steps {
                script {
                    input message: 'Security scans complete. Review the archived reports. Proceed with deployment?', ok: 'Deploy'
                }
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running unit tests..."'
                sh 'python3 -m pytest test_app.py -v || python3 test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker rm -f flask-task1-container || true'
                sh 'docker run -d -p 5500:5500 --name flask-task1-container flask-task1'
                sh 'sleep 3'
                sh 'curl http://localhost:5500'
                sh 'echo "Deployment successful!"'
            }
        }
    }
}
