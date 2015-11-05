from sqlite3 import datetime, Date

class mission_bean(object):
    
    def __init__(self, user_id, title, description, current_track, track_goal, units, start, end, complete, *mission_id):
        self.user_id = str(user_id)
        self.title = str(title)
        self.description = str(description)
        self.current_track = int(current_track)
        self.track_goal = int(track_goal)
        self.units = str(units)
        s = None
        if len(start) > 0:
            dateparts = start.split('/')
            s = datetime.date(int(dateparts[2]),int(dateparts[0]),int(dateparts[1]))
        else:
            s = datetime.date(0,0,0).today()
        self.start = str(Date.strftime(s,"%m/%d/%Y"))
        e = None
        if len(end) > 0:
            dateparts = end.split('/')
            e = datetime.date(int(dateparts[2]),int(dateparts[0]),int(dateparts[1]))
        else:
            e = datetime.date(0,0,0).today()
        self.end = str(Date.strftime(e,"%m/%d/%Y"))
        self.complete = int(complete)