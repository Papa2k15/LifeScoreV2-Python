from flask import Flask
from flask.templating import render_template
lifescore = Flask(__name__)

@lifescore.route('/')
def home_page():
    return render_template('home.html')

@lifescore.route('/register')
def registration():
    return render_template('register.html')

if __name__ == '__main__':
    lifescore.run(debug=True)