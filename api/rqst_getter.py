#!/usr/bin/env python3
from flask import Flask, request
from datetime import datetime
from flask_opentracing import FlaskTracing
from jaeger_client import Config


app = Flask(__name__)
config = Config(config=
{
    'sampler': {'type': 'const', 'param': 1},
    'local_agent':
    {'reporting_host': '172.2.1.5'}
},
    service_name='api_rst_getter'
)
jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer, True, app)


@app.route('/', methods=['GET', 'POST'])
def get_header():
    now = datetime.now()
    print(now)
    file = open('./api_header.log', 'a')
    req_header = request.headers.values()
    time = '\n' + str(now) + '\n'
    file.write(time)
    req_body = request.values

    for items in req_header:
        file.write(' - ')
        print(items)
        file.write(items)
        file.write('\n')
    for items in req_body:
        file.write(' - ')
        print(items, ': ', req_body[items])
        item = str(items)+': '
        file.write(item)
        file.write(req_body[items])

    file.close()

    return "it is what it is"


@app.route('/test')
def test():
    print("This is a test method")
    return ('Yooohooo, you\'re connected to backend\nv2')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)


