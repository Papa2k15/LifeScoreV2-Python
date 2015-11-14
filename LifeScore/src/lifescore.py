from flask import Flask, redirect
from flask.templating import render_template
import hashlib
from flask.globals import request, session
from dao.dao_factory import dao_factory
from beans.user_bean import user_bean
from beans.user_info_bean import user_info_bean
import time
from datetime import date
from beans.mission_bean import mission_bean

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
    results = factory.get_user_dao().add_new_user(user_bean(first_name, last_name, time.strftime("%m/%d/%Y"), email, username, hashlib.sha256(password.encode()).hexdigest())) 
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
        user_info = factory.get_user_info_dao().get_user_info(session.get('logged_user_id'))
        return render_template('user_home.html',uid = session.get('logged_user_id'), userinfo = user_info )
    return redirect("/")

@lifescore.route('/mission_control')
def user_mission_control(): 
    if session.get('logged_user_id'):
        cuser = factory.get_user_dao().get_user(session.get('logged_user_id'))
        return render_template('user_mission_control.html', user = cuser, uid = session.get('logged_user_id'))
    return redirect("/")


@lifescore.route('/settings')
def user_settings():
    if session.get('logged_user_id'):
        cuser = factory.get_user_dao().get_user(session.get('logged_user_id'))
        return render_template('user_settings.html',uid = session.get('logged_user_id'),
            user = cuser, 
            userinfo = factory.get_user_info_dao().get_user_info(session.get('logged_user_id')),
            tenure = (date.today().year - int(cuser.datejoined.split("/")[2])))
    return redirect("/")

@lifescore.route('/logout')
def logout():
    if session.get('logged_user_id'):
        session.pop('logged_user_id', None)
    return redirect('/')

#inline user info update methods
@lifescore.route('/updatebio/', methods=["POST"])
def update_user_bio():
    current = factory.get_user_info_dao().get_user_info(str(request.form['pk']))
    current.bio = request.form['value']
    factory.get_user_info_dao().update_user_info(current)
    return "Updated";

@lifescore.route('/updategender/', methods=["POST"])
def update_user_gender():
    current = factory.get_user_info_dao().get_user_info(str(request.form['pk']))
    current.gender = request.form['value']
    factory.get_user_info_dao().update_user_info(current)
    return "Updated";

#Currently not working
@lifescore.route('/updatedob/', methods=["POST"])
def update_user_dob():
    current = factory.get_user_info_dao().get_user_info(str(request.form['pk']))
    current.dateofbirth = request.form['value']
    factory.get_user_info_dao().update_user_info(current)
    return "Updated";

#Mission routes
@lifescore.route('/add_user_mission/', methods=['POST'])
def add_user_mission():
    if session.get('logged_user_id'):
        title = request.form['title']
        description = request.form['description']
        start = request.form['start']
        goal = request.form['goal']
        units = request.form['units']
        current_track = 0
        end = ''
        complete = 0
        new_user_mission = mission_bean(session.get('logged_user_id'), title, description, current_track, goal, units, start, end, complete)
        return factory.get_mission_dao().add_new_user_mission(new_user_mission)        
    return redirect('/')

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

#html helper functions
def get_reg_username(user_id):
    return factory.get_user_dao().get_user(str(user_id)).username

lifescore.jinja_env.filters['get_reg_username'] = get_reg_username

if __name__ == '__main__':
    lifescore.run(debug=True)