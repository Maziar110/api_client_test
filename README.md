# API - Client to test your infrastructure with docker image
First of all to run this project you should have docker installed on your host then you should just build docker images with the dockerfiles which are included in project and then run the images. 
### Note: **You should first run API container and then run the client**
Also you can commit the docker images and use in your kubernetes. 

# Goal
The goal of this project is to make a simple cloud with one api, one client and a loadbalancer and after all we are going to monitor the loadbalancer with NetData.

**This project has 2 parts:**

## API:

This API gets all requests sent to it and write down on a log file. it gets the body of request and it's headers as well.

## Client:
Constantly sends requests to the api with different bodies and different URLs in every x seconds (mentioned in code) 
since the urls are different, some of them are going to fail and by that we can have our nginx error log for furthur actions.

## How to Run:
run the bash script in the project ;) yeah this easy :)


if you had any question, we can be in touch via:

[maziar.sh110@gmail.com](mailto:maziar.sh110@gmail.com)

[Linkedin](https://www.linkedin.com/in/maziar-shahsavanpour-a4210088/)

[Whatsapp](https://api.whatsapp.com/send?phone=+989156262067)
