from sqlite3 import Date, datetime

class user_info_bean(object):
  
    def __init__(self, bio, dateofbirth, gender, favcolor, *user_id):
        if not user_id:
            self.user_id = None
        else:
            self.user_id = int(user_id[0])
        self.bio = str(bio)
        dob = None
        if len(dateofbirth) > 0:
            dateparts = dateofbirth.split('/')
            dob = datetime.date(int(dateparts[2]),int(dateparts[0]),int(dateparts[1]))
        self.dateofbirth = str(Date.strftime(dob,"%m/%d/%Y"))
        self.gender = str(gender)
        self.favcolor = str(favcolor)