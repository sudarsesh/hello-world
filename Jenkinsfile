pipeline {
    agent {
        docker {
            image 'python:3'
        }
    }} 
    stages {
        stage ('Build') {
            steps {
		        retry(3) {
            	    sh './sample.py'	
    		    }

                sh '''
                   echo "multi line shell step"
                   date 
                '''

        		timeout(time: 2, unit: 'SECONDS') {
        		    sh './sleep_script.py'
                }
            }
        }
        
        stage('Test') {
            sh '''
                pwd
                ls -l
                ./myscript.py
            '''
        }
    }
}
