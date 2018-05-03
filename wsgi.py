from flask import Flask
from flask import render_template

import socket

application = Flask(__name__)


@application.route('/hello')
def hello():
    return 'Hello World!'


@application.route('/')
@application.route('/index')
def index():
    user = {'username': 'Leon'}
    hostname = socket.gethostname()
    return render_template('index.html', title='Flask on OpenShift', user=user, hostname=hostname)


if __name__ == '__main__':
    application.run()
