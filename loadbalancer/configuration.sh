#!/bin/bash
#old=$(cat /etc/nginx/sites-available/api.conf | grep "server api")
#echo $old
#echo $API_IP
#sed -i "s/$old/ server $API_IP;/g" /etc/nginx/sites-available/api.conf
ls /var/log/nginx
apt-get update
apt-get -y install nginx-plus-module-opentracing
nginx -t
service nginx start
