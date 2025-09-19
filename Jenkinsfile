pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling latest code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
                // No pip required
            }
        }

        stage('Test') {
            steps {
                bat 'python demo1_test.py'
            }
        }

        stage('Deploy') {
            steps {
                bat 'python demo1.py'
            }
        }
    }
}
