pipeline {
    agent any
    tools {
        maven 'Maven 3.9.6'
    }
    stages {
        stage('Git Checkout') {
            steps {
                script {
                    git branch: 'main',
                    credentialsId: 'jenhub',
                    url: 'https://github.com/mevine54/jenkins.git'
                }
            }
        }
        stage('Install dependencies') {
            steps {
                bat 'pip  install -r requirements.txt'
            }
        }
        stage('Run python') {
            steps {
                bat 'python app.py'
            }
        }
    }
}