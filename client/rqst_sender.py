import requests
import time,datetime
import random
import os
rand = random

# getting Load-Balancer IP from environment
ip = os.environ['LB_IP']
print(ip)

# Stacks
names = ['John','Maziar','Sara','Albert','Tyler','Chandler','Monika','Michel','Nelson','Gandi','Joey']
projects = ['Dance with wolves', 'Call Trump','Kiss Monika','Watch 8th season of GOT',
            'Wash the dishes', 'Global peace', 'Nuclear Weapon', 'Cooking lunch for Maziar', 'laying down on the couch']
durations = ['1 Day', '1 Week', '1 month', '2days', '4 hours', 'whenever he/she likes']

urls = ['http://'+ip+':8080', 'http://'+ip+':8080'+'/hahaha',
        'http://'+ip+':8080'+'/yooohooo', 'http://'+ip+':8080'+'/what\'sinyourmind',
        'http://'+ip+':8080'+'/wrong']

# Functions
def req_creator():
    name = rand.choice(names)
    project = rand.choice(projects)
    duration = rand.choice(durations)
    rq = {'name':name, 'project':project, 'duration':duration}
    return rq

def url_creator():
    url = rand.choice(urls)

    return url


# Run
while 1:
    time.sleep(15)
    print(datetime.datetime.now())
    url = url_creator()
    body = req_creator()
    
    try:
        requests.post(url= url, data= body)
    except Exception as e:
        print(e)


    #
    # s.enter(10,10,printer())
