pipeline {
    agent any
    stages {
        stage('Git Checkout') }
            steps {
                script {
                    git branch: 'main',
                    credentialsId: 'jenhub',
                    url: 'https://github.com/mevine54/jenkins.git'

                }
            }
        }
    }
}