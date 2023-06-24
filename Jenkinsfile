pipeline{
    agent any

    environment{

        DOCKERHUB_USERNAME = "siddy15"
        APP_NAME = "gitops-argocd-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}" + "/" + "${APP_NAME}"
        REGISTRY_CREDS = "dockerhub"
    }
    stages{
        
        stage('Cleanup workspace'){

            steps{
                script{

                    cleanWs()
                }
            }
        }
        
        stage('Checkout SCM'){

            steps{
                script{
                    git credentialsId: 'github',
                    url: 'https://github.com/siddy15/argocd-gitops.git',
                    branch: 'main'
                }
            }
        }

        stage('Build Docker Image'){

            steps{
                script{
                    docker_image = docker.build "${IMAGE_NAME}"
                    docker_image = docker.build "${DOCKERHUB_USERNAME}/${APP_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
}