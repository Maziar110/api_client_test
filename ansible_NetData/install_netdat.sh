#!/bin/bash

#You should have set password on docker containers
#API container and LoadBalancer container ports should be -
# - the same as what is set in dockerfile and docker compose
docker_name=$(docker ps --format "{{.Names}}")
echo $docker_name
for container in $docker_name
do 
res=$(docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $container)

if [[ $container != *"client_1"* ]]
then
if [[ $container == *"api_1"* ]]
then 
port=201
fi
if [[ $container == *"loadbalancer_1"* ]]
then 
port=203
fi
echo $res >> ./host
echo $container
echo $res:$port

    ssh-copy-id -f root@$res -p $port
fi

done
