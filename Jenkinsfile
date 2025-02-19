pipeline {
    agent any
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
        stage('Build Maven') {
            steps {
                bat 'mvn clean package'
            }
        }
    }
}