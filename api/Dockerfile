FROM debian:latest
LABEL maintainer="maziar.sh110@gmail.com"
RUN mkdir /var/project/
RUN mkdir /var/project/api
RUN apt update
RUN apt-get install -y python3
RUN apt-get install -y ssh
RUN apt-get install -y curl
RUN curl -o ./get-pip.py https://bootstrap.pypa.io/get-pip.py 
RUN apt-get install -y python3-distutils 
RUN python3 ./get-pip.py
COPY ./requirements.txt .
COPY ./fire.sh /var/project/fire.sh
RUN pip3 install -r ./requirements.txt
EXPOSE 5000
EXPOSE 201
RUN chmod +x /var/project/fire.sh
ENV FLASK_APP='/var/project/api/rqst_getter.py'
CMD flask run --host=0.0.0.0
