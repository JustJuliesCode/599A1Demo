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
                sh 'pip3 install pytest'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'pytest demo1_test.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'python demo1.py'
            }
        }
        
    }
}
