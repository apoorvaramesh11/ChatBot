pipeline{
    agent any

    environment{
        IMG_NAME = "apoorvar12/chatbot:${GIT_COMMIT}"
    }

    stages{
        stage('checkout'){
            steps{
                echo 'Cloning the git repository'
                git branch: 'main', url: 'https://github.com/apoorvaramesh11/ChatBot.git'
            }
        }
        stage('build'){
            steps{
	
                echo 'Building docker image'
                sh 'docker build -t $IMG_NAME .'
            }
        }
	stage('docker run'){
            steps{
                echo 'running docker container'
                sh 'docker run -d -p 8000:5000 $IMG_NAME'
            }
        }
        
    }
}
