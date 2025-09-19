pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling latest code...'
                git branch : 'main', url: 'https://github.com/JustJuliesCode/599A1Demo.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
post {
    success {
        bat 'echo "build successful"'
    }
    failure {
        bat 'echo "build failure"'
    }
}
