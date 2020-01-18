FROM debian:latest
RUN apt install python3
RUN curl -o ./get-pip.py https://bootstrap.pypa.io/get-pip.py 
COPY ../requirements.txt .
RUN pip3 install -r ./requirements.txt
COPY ./rqst_sender.py /var/project/client/
CMD python3 rqst_sender.py

#to build this docker image run: "docker build -t <name:version> ." and then you can run this image with: "docker run <name:version>"