import sqlite3 as lite
from loaders.user_info_loader import user_info_loader

class user_info_dao:
    
    def __init__(self):
        self.user_info_loader_obj = user_info_loader()
        self.database_connector = lite.connect('lifescore.db')

    def add_new_user_info(self, user_info_bean):
        con = None
        try:
            con = self.database_connector
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO userinfo (bio) VALUES(?)",
                            (user_info_bean.bio))
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
                return self.user_info_loader_obj.load_single(cur)
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
                    "UPDATE userinfo SET bio = ? WHERE userID = ?",
                    (user_info_bean.bio,user_info_bean.user_id))
                con.commit()
                return True
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()