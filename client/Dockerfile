FROM debian:latest
LABEL maintainer="maziar.sh110@gmail.com"
RUN mkdir /var/project/
RUN mkdir /var/project/client
RUN apt update
RUN apt-get install -y python3
RUN apt-get install -y curl
RUN apt-get install -y ssh
RUN curl -o ./get-pip.py https://bootstrap.pypa.io/get-pip.py 
RUN apt-get install -y python3-distutils 
RUN python3 ./get-pip.py
COPY ./rqst_sender.py /var/project/client
COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt
EXPOSE 202
CMD ["python3", "/var/project/client/rqst_sender.py"]

#to build this docker image run: "docker build -t <name:version> ." and then you can run this image with: "docker run <name:version>"