import sqlite3 as lite
from loaders.user_loader import user_loader

class user_dao:
    
    def __init__(self):
        self.user_loader_obj = user_loader()
        self.database_connector = lite.connect('lifescore.db')

    def add_new_user(self, user_bean):
        con = None
        try:
            con = self.database_connector
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO user (first_name, last_name, username, email, password) VALUES(?, ?, ?, ?, ?)",
                            (user_bean.first_name, user_bean.last_name,user_bean.username,user_bean.email,user_bean.password))
                con.commit()
                return True, "Successfully registered! You may now log in " + user_bean.username
        except lite.Error, e:
            return False, str(e)
        finally:
            if con:
                con.close()
        
    def get_user(self, _userID):
        con = None
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
    
    def get_registered_user(self, _username, _password):
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute("SELECT * FROM user WHERE username = ? AND password = ?", (_username,_password))
                con.commit()
                return self.user_loader_obj.load_single(cur)
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()
    
    def remove_user(self, _userID):
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute("DELETE FROM user WHERE userID = ?", (_userID,))     
                con.commit()     
                return True, "Successfully removed user."
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
                    "UPDATE user SET first_name = ?, last_name = ?, username = ?, email = ?, password = ? WHERE userID = ?",
                    (user_bean.first_name, user_bean.last_name ,user_bean.username,user_bean.email,user_bean.password,user_bean.user_id))
                con.commit()
                return True, "Successfully updated user information."
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

     
    def query_username_exists(self, _username):
        search_query = _username.rstrip().split(' ');
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                for q in search_query:
                    querybuilder =  " SELECT * FROM user WHERE username LIKE '" + q + "'" 
                    cur.execute(querybuilder)
                    con.commit()
                data = cur.fetchall()
                if len(data) > 0:
                    return True
                return False
        except lite.Error, e:
            return False,str(e)
        finally:
            cur.close()
            con.close()
            
    def query_email_exists(self, _email):
        search_query = _email.rstrip();
        con = None
        try:
            con = self.database_connector
            with con:
                con.rollback()
                cur = con.cursor()
                cur.execute(" SELECT * FROM user WHERE email LIKE '" + search_query + "'")
                con.commit()
                data = cur.fetchall()
                if len(data) > 0:
                    return True
                return False
        except lite.Error, e:
            return False, str(e)
        finally:
            cur.close()
            con.close()
                
# search user database
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
