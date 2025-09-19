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
                sh 'pip install pytest'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest demo1_test.py'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python demo1.py'
            }
        }
    }
}
