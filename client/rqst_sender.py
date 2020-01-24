import requests
import time,datetime
import random
rand = random

# Stacks
names = ['John','Maziar','Sara','Albert','Tyler','Chandler','Monika','Michel','Nelson','Gandi','Joey']
projects = ['Dance with wolves', 'Call Trump','Kiss Monika','Watch 8th season of GOT',
            'Wash the dishes', 'Global peace', 'Nuclear Weapon', 'Cooking lunch for Maziar', 'laying down on the couch']
durations = ['1 Day', '1 Week', '1 month', '2days', '4 hours', 'whenever he/she likes']

urls = ['http://172.17.0.13:81', 'http://172.17.0.13:81/hahaha',
        'http://172.17.0.13:81/yooohooo', 'http://172.17.0.13:81/what\'sinyourmind',
        'http://172.17.0.13/wrong','http://api.local']

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
    time.sleep(1)
    print(datetime.datetime.now())
    url = url_creator()
    body = req_creator()
    requests.post(url= url, data= body)


    #
    # s.enter(10,10,printer())
