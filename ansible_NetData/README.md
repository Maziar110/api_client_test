# Why We didn't install netdata while creating docker images?

**Simple answer: ** 
We wanted to try Ansible here. remeber that it's a simulated place to try your tools so the more tools you can use here, the more tests you can perform.

## what you have to do before run the installation?
1- Go inside each container and set a password via `docker exec -it <container name> /bin/bash`
and then write `passwd root` to set new password
2- Create a ssh key via `ssh-keygen -t rsa`
(We need this because then we add the key into containers in order to be able to work with ansible)

** After all, run install_netdata.sh **
## What if you're not interested to install NetData with Ansible?
You can add below lines into your docker files(the container you want to have NetData on):

`RUN git clone https://github.com/firehol/netdata.git ~/netdata `

`~/netdata/netdata-installer.sh`
and after your hosts came up, you simply can start NetData service with `docker exec <container name> service netdata start`

hope it works for you. Contact me if there was anything wrong

