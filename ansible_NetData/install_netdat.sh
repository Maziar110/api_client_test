#!/bin/bash

#You should have set password on docker containers
docker_name=$(docker ps --format "{{.Names}}")
echo $docker_name
for container in $docker_name
do 
# If you want not to install netdata on client, you can add an IF condition
res=$(docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $container)
echo $res >> ./ansible/host
ssh-copy-id -f root@$res
done
