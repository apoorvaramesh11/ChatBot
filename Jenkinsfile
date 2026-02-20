pipeline{
    agent any

    environment{
        IMG_NAME = "chatbot-${GIT_COMMIT}"
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
        
    }
}
