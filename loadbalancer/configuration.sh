#!/bin/bash
#old=$(cat /etc/nginx/sites-available/api.conf | grep "server api")
#echo $old
#echo $API_IP
#sed -i "s/$old/ server $API_IP;/g" /etc/nginx/sites-available/api.conf
service nginx restart
tail -f /var/log/nginx/api/access.log