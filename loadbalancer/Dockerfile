FROM debian
RUN apt update
RUN apt install -y nginx
RUN apt install -y ssh
RUN rm /etc/nginx/nginx.conf
COPY ./nginx.conf /etc/nginx/
COPY ./api.conf /etc/nginx/sites-available
RUN ln -s /etc/nginx/sites-available/api.conf /etc/nginx/sites-enabled/
RUN mkdir /var/log/nginx/api/
RUN service nginx restart
