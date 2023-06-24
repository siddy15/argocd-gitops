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
                    branch: 'worker'
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

        stage('Push Docker Image'){

            steps{
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'Password', usernameVariable: 'username')]) {
                    // sh ‘docker push $BUILD_NUMBER’
                    echo 'Login Success'
                    // sh ‘docker tag $BUILD_NUMBER’ + ' ' + ‘$DOCKERHUB_USERNAME/$BUILD_NUMBER’
                    // sh ‘docker rmi $BUILD_NUMBER’
                    sh 'docker push $DOCKERHUB_USERNAME/$APP_NAME'
                    sh 'docker push $DOCKERHUB_USERNAME/$APP_NAME:$IMAGE_TAG'
                }
            }
        }
    }
}