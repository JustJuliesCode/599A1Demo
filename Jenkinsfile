pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                echo 'Pulling latest code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest demo1_test.py'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 demo1.py'
            }
        }
    }
}
