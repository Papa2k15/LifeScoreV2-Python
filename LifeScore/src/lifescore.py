from flask import Flask, redirect
from flask.templating import render_template
import hashlib
from flask.globals import request
from dao.dao_factory import dao_factory
from beans.user_bean import user_bean
from beans.user_info_bean import user_info_bean

lifescore = Flask(__name__)
factory = dao_factory.get_instance()

@lifescore.route('/')
def login_page():
    return render_template('index.html')

@lifescore.route('/register')
def registration():
    return render_template('register.html')

@lifescore.route('/register_user/', methods=['POST'])
def register_new_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    results = factory.get_user_dao().add_new_user(user_bean(first_name, last_name, email, username, hashlib.sha256(password.encode()).hexdigest()))
    factory.get_user_info_dao.add_new_user_info(user_info_bean(""))
    return_message = results[1]
    return_error = not results[0]
    return render_template('index.html',message=return_message,error=return_error)

@lifescore.route('/login/',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = factory.get_user_dao().get_registered_user(username,hashlib.sha256(password.encode()).hexdigest())
    user_info = factory.get_user_info_dao().get_user_info(user.user_id)
    if user != None:
        return render_template('user_home.html',username=username,uid = user.user_id, userinfo = user_info )
    return render_template('index.html',message="Invalid credentials, try again",error=True)

@lifescore.route('/logout')
def logout():
    return redirect('/')

#inline user info update methods
@lifescore.route('/update/', methods=["POST"])
def update_user_info():
    factory.get_user_info_dao().update_user_info(user_info_bean(request.form['value'],str(request.form['pk'])))
    return "Updated";

#Registration Helper Methods
@lifescore.route('/check_username', methods=['GET'])
def check_username():
    query = request.args.get('q')
    results = factory.get_user_dao().query_username_exists(query) 
    if results == True:
        return "<div class='alert-danger'>User name '" + query + "' is already in use</div>"
    return ""   

@lifescore.route('/check_email', methods=['GET'])
def check_email():
    query = request.args.get('q')
    results = factory.get_user_dao().query_email_exists(query) 
    if results == True:
        return "<div class='alert-danger'>Email '" + query + "' is already in use by another user</div>"
    return ""

if __name__ == '__main__':
    lifescore.run(debug=True)