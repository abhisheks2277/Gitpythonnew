pipeline {
    agent any

    stages {
        stage('Merge Develop into Master') {
            steps {
                bat '''
                git checkout master
                git pull origin master
                git merge --no-ff origin/develop
                git push origin master
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
