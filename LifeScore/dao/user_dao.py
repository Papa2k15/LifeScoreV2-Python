import sqlite3 as lite
from loaders.user_loader import user_loader

class user_dao:
    
    def __init__(self, database_connector):
        self.user_loader_obj = user_loader()
        self.database_connector = database_connector

    def add_new_user(self, user_bean):
        try:
            con = self.database_connector
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO user (name, username, email, password) VALUES(?, ?, ?, ?)",
                            (user_bean.name,user_bean.username,user_bean.email,user_bean.password))
                con.commit()
                return True
        except lite.Error, e:
            return False, str(e)
        finally:
            if con:
                con.close()
        
    def getUser(self, _userID):
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute("SELECT * FROM user WHERE userID = ?", (_userID,))
                con.commit()
                return self.user_loader_obj.load_single(cur)
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()
    
    def remove_user(self, _userID):
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute("DELETE FROM user WHERE userID = ?", (_userID,))     
                con.commit()     
                return True
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()
     
    def update_user(self, user_bean):
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute(
                    "UPDATE user SET name = ?, username = ?, email = ?, password = ? WHERE userID = ?",
                    (user_bean.name,user_bean.username,user_bean.email,user_bean.password,user_bean.user_id))
                con.commit()
                return True
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()

    def get_all_users(self):
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute("SELECT * FROM user")
                con.commit()
                return user_loader.load_list(self, cur)
        except lite.Error, e:
            return str(e)
     
        finally:
            cur.close()
            con.close()

     
#     # search user database
#     def queryUserDatabase(_database, _query):
#         search_query = _query.rstrip().split(' ');
#         con = None
#         try:
#             # connect to sqlite3
#             con = lite.connect(_database)
#             with con:
#                 con.rollback()
#                 cur = con.cursor()
#                 for q in search_query:
#                     querybuilder =  "SELECT * FROM user WHERE userID LIKE '" + q + "%'" \
#                                     " UNION" \
#                                     " SELECT * FROM user WHERE first_name LIKE '" + q + "%'" \
#                                     " UNION" \
#                                     " SELECT * FROM user WHERE last_name LIKE '" + q + "%'" \
#                                     " UNION" \
#                                     " SELECT * FROM user WHERE email LIKE '" + q + "%'"   \
#                                     " UNION " \
#                                     "SELECT * FROM user WHERE userID LIKE '%" + q + "%'" \
#                                     " UNION" \
#                                     " SELECT * FROM user WHERE first_name LIKE '%" + q + "%'" \
#                                     " UNION" \
#                                     " SELECT * FROM user WHERE last_name LIKE '%" + q + "%'" \
#                                     " UNION" \
#                                     " SELECT * FROM user WHERE email LIKE '%" + q + "%'" \
#                                     " UNION " \
#                                      "SELECT * FROM user WHERE userID LIKE '%" + q + "'" \
#                                     " UNION" \
#                                     " SELECT * FROM user WHERE first_name LIKE '%" + q + "'" \
#                                     " UNION" \
#                                     " SELECT * FROM user WHERE last_name LIKE '%" + q + "'" \
#                                     " UNION" \
#                                     " SELECT * FROM user WHERE email LIKE '%" + q + "'" 
#                     cur.execute(querybuilder)
#                     con.commit()
#                 data = cur.fetchall()
#                 if len(data) > 0:
#                     return data
#                 return 'no results'
#         except lite.Error, e:
#             return str(e)
#         finally:
#             cur.close()
#             con.close()
