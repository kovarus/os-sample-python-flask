from flask import Flask
from flask import render_template

application = Flask(__name__)

@application.route('/hello')
def hello():
    return 'Hello World!'

@application.route('/')
@application.rout('/index')
def index():
    user = {'username': 'Leon'}
    return render_template('index.html', title='home', user=user)

if __name__ == '__main__':
    application.run()
