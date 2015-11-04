from flask import Flask, redirect
from flask.templating import render_template
import hashlib
from flask.globals import request, session
from dao.dao_factory import dao_factory
from beans.user_bean import user_bean
from beans.user_info_bean import user_info_bean

lifescore = Flask(__name__)
lifescore.secret_key = 'lifescore'
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
    if False not in results:
        factory.get_user_info_dao().add_new_user_info(user_info_bean("","","",""))
    return_message = results[1]
    return_error = not results[0]
    return render_template('index.html',message=return_message,error=return_error)

@lifescore.route('/login/',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = factory.get_user_dao().get_registered_user(username,hashlib.sha256(password.encode()).hexdigest())
    if user != None:
        session['logged_user_id'] = str(user.user_id)
        return redirect("/home")
    return render_template('index.html',message="Invalid credentials, try again",error=True)

@lifescore.route('/home')
def user_home(): 
    if session.get('logged_user_id'):
        user = factory.get_user_dao().get_user(session.get('logged_user_id'))
        user_info = factory.get_user_info_dao().get_user_info(session.get('logged_user_id'))
        return render_template('user_home.html',username=user.username,uid = session.get('logged_user_id'), userinfo = user_info )
    return redirect("/")

@lifescore.route('/settings')
def user_settings():
    if session.get('logged_user_id'):
        return render_template('user_settings.html')
    return redirect("/")

@lifescore.route('/logout')
def logout():
    if session.get('logged_user_id'):
        session.pop('logged_user_id', None)
    return redirect('/')

#inline user info update methods
@lifescore.route('/updatebio/', methods=["POST"])
def update_user_info():
    current = factory.get_user_info_dao().get_user_info(str(request.form['pk']))
    current.bio = request.form['value']
    factory.get_user_info_dao().update_user_info(current)
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