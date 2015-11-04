import sqlite3 as lite
from beans.user_info_bean import user_info_bean

class user_info_dao:
    
    def __init__(self):
        self.database_connector = lite.connect("lifescore.db")

    def add_new_user_info(self, user_info_bean):
        con = None
        try:
            con = self.database_connector
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO userinfo (bio, dateofbirth, gender, favcolor) VALUES(?)",
                            (user_info_bean.bio, user_info_bean.dateofbirth, user_info_bean.gender, user_info_bean.favcolor))
                con.commit()
                return True
        except lite.Error, e:
            return False, str(e)
        finally:
            if con:
                con.close()
        
    def get_user_info(self, _userID):
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute("SELECT * FROM userinfo WHERE userID = ?", (_userID,))
                con.commit()
                single_user_info_data = cur.fetchone()
                if single_user_info_data != None:
                    return user_info_bean(single_user_info_data[1],single_user_info_data[2],single_user_info_data[3],single_user_info_data[4],single_user_info_data[0])
                return single_user_info_data
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()
    
    def remove_user_info(self, _userID):
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute("DELETE FROM userinfo WHERE userID = ?", (_userID,))     
                con.commit()     
                return True
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()
     
    def update_user_info(self, user_info_bean):
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute(
                    "UPDATE userinfo SET bio = ?, dateofbirth = ?, gender = ?, favcolor = ? WHERE userID = ?",
                    (user_info_bean.bio,user_info_bean.dateofbirth, user_info_bean.gender, user_info_bean.favcolor, user_info_bean.user_id))
                con.commit()
                return True
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()