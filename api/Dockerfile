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
COPY ./rqst_getter.py /var/project/api/
COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt
EXPOSE 5000
EXPOSE 22
ENV FLASK_APP='/var/project/api/rqst_getter.py'
CMD flask run --host=0.0.0.0
#to build this docker image run: "docker build -t <name:version> ." and then you can run this image with: "docker run <name:version>"