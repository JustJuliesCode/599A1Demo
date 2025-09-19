pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling latest code...'
                
            }
        }

        stage('Build') {
            steps {
                echo 'Building...'
                bat 'pip3 install pytest'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                bat 'pytest demo1_test.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                bat 'python demo1.py'
            }
        }
        
    }
}
