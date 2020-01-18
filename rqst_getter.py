from flask import Flask, request
from datetime import datetime
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)