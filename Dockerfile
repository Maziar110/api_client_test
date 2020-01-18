FROM debian:latest
RUN mkdir /var/project/api
RUN mkdir /var/project/client
RUN apt install python3
RUN curl -o ./get-pip.py https://bootstrap.pypa.io/get-pip.py 
COPY ./rqst_getter.py /var/project/api/
COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt
CMD [ "python3","/var/project/api/rqst_getter.py" ]
#to build this docker image run: "docker build -t <name:version> ." and then you can run this image with: "docker run <name:version>"