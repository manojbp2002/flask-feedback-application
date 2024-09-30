#!bin/bash
set -e

#pull the docker image from dockerhub
docker pull manojbp609/simple-feedback-app

#run the docker iamge as a container
docker run -d -p 5000:5000 manojbp609/simple-feedback-app


