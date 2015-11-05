from sqlite3 import datetime, Date

class user_bean(object):

    def __init__(self, first_name, last_name, datejoined, email, username, password, *user_id):
        if not user_id:
            self.user_id = None
        else:
            self.user_id = int(user_id[0])
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        dj = None
        if len(datejoined) > 0:
            dateparts = datejoined.split('/')
            dj = datetime.date(int(dateparts[2]),int(dateparts[0]),int(dateparts[1]))
        self.datejoined = str(Date.strftime(dj,"%m/%d/%Y"))
        self.email = str(email)
        self.username = str(username)
        self.password= str(password)
        
        