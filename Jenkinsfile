pipeline {
    agent any
    stages {
        stage('Git Checkout') }
            steps {
                script {
                    git branch: 'main',
                    credentialsId: 'jenkins_github_PAT',
                    url: 'https://github.com/mevine54/jenkins.git'

                }
            }
        }
    }
}