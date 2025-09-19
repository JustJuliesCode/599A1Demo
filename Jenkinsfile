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
                bat '"C:\Users\julie\AppData\Local\Programs\Python\Python39\python.exe" demo1_test.py'
            }
        }

        stage('Deploy') {
            steps {
                bat '"C:\Users\julie\AppData\Local\Programs\Python\Python39\python.exe" demo1.py'
            }
        }

    }
}
