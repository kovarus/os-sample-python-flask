from flask import Flask
from flask import render_template

import socket
import datetime


application = Flask(__name__)


@application.route('/hello')
def hello():
    return 'Hello World!'


@application.route('/')
@application.route('/index')
def index():
    now = datetime.datetime.now()
    user = {'username': 'User'}
    hostname = socket.gethostname()
    return render_template('index.html', title='Flask on OpenShift',
                           user=user,
                           hostname=hostname,
                           time=now.strftime('%m-%d-%Y %H:%M'))


if __name__ == '__main__':
    application.run()
