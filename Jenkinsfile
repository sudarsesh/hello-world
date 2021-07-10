pipeline {
    agent {
        dockerfile {
            dir 'Dockerfiles'
            file 'Dockerfile.maven'
            label 'agent1'
        }
    }

    stages {
        stage('GIT SCM') {
            steps {
                sh 'mvn -version'
            }
        }
    }
}