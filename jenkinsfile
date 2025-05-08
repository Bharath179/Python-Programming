pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/my-python-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Specific Tests') {
            steps {
                // Only run tests from test_scripts/
                sh 'pytest pytestsession/ --html=report.html --self-contained-html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }
}
