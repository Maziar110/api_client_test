FROM debian:latest
RUN mkdir /var/project/
RUN mkdir /var/project/client
RUN apt update
RUN apt install -y python3
RUN apt install -y curl
RUN curl -o ./get-pip.py https://bootstrap.pypa.io/get-pip.py 
RUN apt install -y python3-distutils 
RUN python3 ./get-pip.py
COPY ./rqst_sender.py /var/project/client
COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt
CMD ["python3", "/var/project/client/rqst_sender.py"]

#to build this docker image run: "docker build -t <name:version> ." and then you can run this image with: "docker run <name:version>"