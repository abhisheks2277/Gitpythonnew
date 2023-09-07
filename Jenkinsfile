pipeline {
    agent any
    
    stages {
        stage('Create Merge Request') {
            steps {
                script {
                    // Create a merge request (pull request) from 'develop' to 'master'
                    sh 'git checkout develop'
                    sh 'git pull origin develop'
                    sh 'git checkout -b feature-branch' // Create and switch to a new feature branch
                    // Make your code changes here
                    sh 'git add .'
                    sh 'git commit -m "Your commit message"'
                    sh 'git push origin feature-branch' // Push changes to the feature branch
                    sh 'git checkout master'
                    sh 'git pull origin master'
                    sh 'git merge --no-ff feature-branch'
                    sh 'git push origin master'
                    
                    // Optionally, delete the feature branch after merging
                    sh 'git branch -d feature-branch'
                    sh 'git push origin --delete feature-branch'
                }
            }
        }
    }
    
    post {
        success {
            // Actions to take when the pipeline succeeds (e.g., notifications)
            echo 'Pipeline succeeded!'
            // You can add additional actions here, such as sending notifications or triggering other jobs
        }
        failure {
            // Actions to take when the pipeline fails (e.g., notifications)
            echo 'Pipeline failed!'
            // You can add additional actions here, such as sending failure notifications
        }
    }
}
