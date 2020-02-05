FROM debian
LABEL maintainer="maziar.sh110@gmail.com"
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y ssh
RUN rm /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx/
COPY ./api.conf /etc/nginx/sites-available
COPY ./configuration.sh .
RUN ln -s /etc/nginx/sites-available/api.conf /etc/nginx/sites-enabled/
RUN mkdir /var/log/nginx/api/
#ENV API_IP='172.2.1.2:5000'
CMD bash ./configuration.sh
EXPOSE 8080
