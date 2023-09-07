pipeline {
    agent any

    stages {
        stage('Merge Develop into Master') {
            steps {
                script {
                    // Ensure you are on the 'master' branch
                    sh 'git checkout master'
                    sh 'git pull origin master'

                    // Merge 'develop' into 'master' and retain all commit history
                    sh 'git merge --no-ff origin/develop'

                    // Push the changes to 'origin'
                    sh 'git push origin master'
                }
            }
        }
    }

    post {
        success {
            // Actions to take when the pipeline succeeds (e.g., notifications)
            echo 'Pipeline succeeded!'
        }
        failure {
            // Actions to take when the pipeline fails (e.g., notifications)
            echo 'Pipeline failed!'
        }
    }
}
