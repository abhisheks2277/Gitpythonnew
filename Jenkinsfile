pipeline {
    agent any

    environment {
        SHELL = 'cmd'
    }

    stages {
        stage('Create Merge Request') {
            steps {
                script {
                    // Ensure you are on the 'develop' branch
                    sh 'git checkout develop'
                    sh 'git pull origin develop'

                    // Create and switch to a new feature branch
                    sh 'git checkout -b feature-branch'

                    // Make your code changes here
                    // ...

                    // Commit and push your changes
                    sh 'git add .'
                    sh 'git commit -m "Your commit message"'
                    sh 'git push origin feature-branch'

                    // Create the merge request (pull request)
                    // Replace 'YOUR_MERGE_REQUEST_TITLE' and 'YOUR_MERGE_REQUEST_DESCRIPTION' with your desired values
                    sh 'git request-pull -p origin/develop feature-branch -m "YOUR_MERGE_REQUEST_TITLE" "
