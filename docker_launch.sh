#!/bin/bash

# rm docker image
echo %%%%%% LIST DOCKER IMAGE %%%%%%%
docker image ls
echo %%%%%% REMOVE DANGLING DOCKER IMAGE %%%%%%%
docker rmi -f $(docker images -q -a -f dangling=true)
echo %%%%%% REMOVE DOCKER CONTAINER %%%%%%%
docker rm mountainpeaks_database
docker rm mountainpeaks_backend
echo %%%%%% REMOVE DOCKER IMAGE %%%%%%%
docker rmi mountainpeaks_database
docker rmi mountainpeaks_backend
echo %%%%%% REBUILT and START DOCKER COMPOSE %%%%%%%
docker-compose up --build -V
