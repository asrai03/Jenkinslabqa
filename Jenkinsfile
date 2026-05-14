pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building the project..."'
                sh 'ls -la'
                sh 'touch buildArtifact.txt'
                sh 'echo "Build complete" > buildArtifact.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
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
        stage('Clone Task 1') {
            steps {
                sh 'rm -rf dockerfileexercise'
                sh 'git clone https://gitlab.com/Reece-Elder/dockerfileexercise.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                dir('dockerfileexercise/Task1') {
                    sh '''
                        cat > Dockerfile << 'EOF'
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask==2.1.0 werkzeug==2.1.0
ENV YOUR_NAME=Amsrai
EXPOSE 5500
ENTRYPOINT ["python", "app.py"]
EOF
                    '''
                    sh 'docker build -t flask-task1 .'
                }
            }
        }
        stage('Deploy Flask App') {
            steps {
                sh 'docker rm -f flask-task1-container || true'
                sh 'docker run -d -p 5500:5500 --name flask-task1-container flask-task1'
                sh 'sleep 3'
                sh 'curl http://localhost:5500'
            }
        }
    }
}
