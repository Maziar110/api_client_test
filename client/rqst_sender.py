import requests
import time,datetime
import random
rand = random

# Stacks
names = ['Maziar','Vahid\'s','MohamadReza','Yashar','Hamed','Atena','Alireza','Mehdi\'s','Sharare','Hamid','Mostafa']
projects = ['Servers optimization', 'Alerting systems','Ansible Tags',
            'Codes review', 'Security check', 'Nuclear Weapon', 'Config test', 'Follow up issues']
durations = ['1 Day', '1 Week', '1 month', '2days', '4 hours', 'whenever he/she likes']

urls = ['http://127.0.0.1:5000', 'http://127.0.0.1:5000/hahaha',
        'http://127.0.0.1:5000/yooohooo', 'http://127.0.0.1:5000/what\'sinyourmind',
        'http://127.0.0.1/wrong','http://127.0.0.1']

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
