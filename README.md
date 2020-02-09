# API - Client to test your infrastructure with docker image
First of all to run this project you should have docker installed on your host then you should just build docker images with the dockerfiles which are included in project and then run the images. 
### Note: **You should first run API container and then run the client**
Also you can commit the docker images and use in your kubernetes. 

# Goal
The goal of this project is to make a simple, simulated space working like a cloud with (at least)one API node which gets every request and do something, (at least) one client which sends requests to a loadblancer and a loadbalancer which handles the requests and pass them to API node.
after all we are going to monitor the loadbalancer (Or any part of the project we want) with NetData.
Also you can do your tests on this space easily.

**This project has 2 parts:**

## API:

This API gets all requests sent to it and write down on a log file. it gets the body of request and it's headers as well.
You can scale up This node just by editing bash script and using docker-compose commands according to [this help](https://docs.docker.com/compose/reference/scale/)

## Client:
Constantly sends requests to the api with different bodies and different URLs in every x seconds (mentioned in code) 
since the urls are different, some of them are going to fail and by that we can have our nginx error log for furthur actions.

## How to Run:
run the bash script in the project ;) yeah this easy :)

![Project review](https://raw.github.com/Maziar110/api_client_test/project.jpg)
if you had any question, we can be in touch via:

[maziar.sh110@gmail.com](mailto:maziar.sh110@gmail.com)

[Linkedin](https://www.linkedin.com/in/maziar-shahsavanpour-a4210088/)

[Whatsapp](https://api.whatsapp.com/send?phone=+989156262067)
