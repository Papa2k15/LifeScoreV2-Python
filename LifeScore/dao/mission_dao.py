import sqlite3 as lite
from beans.mission_bean import mission_bean

class mission_dao:
    
    def __init__(self):
        self.database_connector = lite.connect("lifescore.db")

    def add_new_user_mission(self, mission_bean):
        con = None
        try:
            con = self.database_connector
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO mission (userID, title, description, current_track, track_goal, units, start, end, complete) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (mission_bean.user_id,mission_bean.title,mission_bean.description,mission_bean.current_track,mission_bean.track_goal,mission_bean.units,mission_bean.start,mission_bean.end,mission_bean.complete))
                con.commit()
                return True
        except lite.Error, e:
            return False, str(e)
        finally:
            if con:
                con.close()
        
    def get_all_missions_for_user(self, _userID):
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute("SELECT * FROM mission WHERE userID = ?", (_userID,))
                con.commit()
                multiple_mission_data = cur.fetchall()
                mission_list = []
                for mission in multiple_mission_data:
                    mission_list.append(mission_bean(mission[1],mission[2],mission[3],mission[4],mission[5],mission[6],mission[7],mission[8],mission[0]))
                return mission_list
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()
    
    def remove_user_mission(self, _userID, _missionID):
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute("DELETE FROM mission WHERE userID = ? and missionID = ?", (_userID,_missionID))     
                con.commit()     
                return True, "Successfully removed mission."
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()
     
    def update_user_mission(self, mission_bean):
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute(
                    "UPDATE mission SET title = ?, description = ?, current_track = ?, track_goal = ?, units = ?, start = ?, end = ?, complete = ? WHERE userID = ? and missionID = ?",
                    (mission_bean.title,mission_bean.description,mission_bean.current_track,mission_bean.track_goal,mission_bean.units,mission_bean.complete,mission_bean.user_id,mission_bean.mission_id))
                con.commit()
                return True, "Successfully updated user information."
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()
