from flask import Flask
from flask.templating import render_template
import hashlib
from flask.globals import request
from dao.dao_factory import dao_factory
from beans.user_bean import user_bean

lifescore = Flask(__name__)
factory = dao_factory.get_instance()

@lifescore.route('/')
def home_page():
    return render_template('home.html')

@lifescore.route('/register')
def registration():
    return render_template('register.html')

@lifescore.route('/register_user/', methods=['POST'])
def register_new_user():
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['pass']
    results = ""
    if factory.get_user_dao().add_new_user(user_bean(name, email, username, hashlib.sha256(password.encode()).hexdigest())):
        results = "Successfully register!"
    else:
        results = "Error with registering. Try again."
    return render_template('home.html',message=results)
    

if __name__ == '__main__':
    lifescore.run(debug=True)