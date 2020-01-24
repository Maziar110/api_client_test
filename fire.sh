#!/bin/bash
api_ip='172.17.0.14'
client_ip='172.17.0.12'
loadbalancer_ip='172.17.0.13'
docker build -t api_test .
docker build -t client_test ./client/
docker build -t loadbalancer ./loadbalancer/
docker run -it -d --name api_test -p $api_ip:8000:5001 -p 201:22 api_test
printf "all:\n api:\n hosts:\n""\t"$api_ip >> ./hosts_inventory.yml
docker run -it -d --name client_test -p $client_ip:8000:5002 -p 202:22 client_test
printf "client:\n hosts:\n""\t"$client_ip >> ./hosts_inventory.yml
docker run -it -d --name loadbalancer -p $loadbalancer:80:80 loadbalancer
printf "loadbalancer:\n hosts:\n""\t"$loadbalancer_ip >> ./hosts_inventory.yml

