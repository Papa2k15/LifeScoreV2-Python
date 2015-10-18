import sqlite3 as lite
from beans.user_bean import user_bean
from loaders.user_loader import user_loader


# this will need to be changed to use google auth
def add_new_user(_database, user_bean):
    con = None
    try:
        # connect to sqlite3
        con = lite.connect(_database)
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO user (name, username, email, password) VALUES(?, ?, ?, ?)",
                        (user_bean.name,user_bean.username,user_bean.email,user_bean.password))
            con.commit()
        return True
    except lite.Error, e:
        return False, e
    finally:
        if con:
            con.close()


# get user information from the database
def getUser(_database, _userID):
    con = None
    try:
        # connect to sqlite3
        con = lite.connect(_database)
        with con:
            con.rollback()
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE userID = ?", (_userID,))
            con.commit()
            return user_loader.load_single(cur)
    except lite.Error, e:
        return str(e)

    finally:
        cur.close()
        con.close()

# remove User from system
def removeUser(_database, _userID):
    con = None
    try:
        # connect to sqlite3
        con = lite.connect(_database)
        with con:
            con.rollback()
            cur = con.cursor()
            cur.execute("DELETE FROM user WHERE userID = ?", (_userID,))

            cur.execute("SELECT * FROM user WHERE userID = ?", (_userID,))
            con.commit()
            data = cur.fetchall()

        if len(data) > 0:
            return 'Error while removing'
        else:
            return 'Remove Successful'

    except lite.Error, e:
        return str(e)

    finally:
        cur.close()
        con.close()


# update user information
def updateUser(_database, _userID, _firstName, _lastName, _role, _dateOfBirth, _dateStarted, _gender, _userBio,
               _pictureURL):
    con = None
    try:
        # connect to sqlite3
        con = lite.connect(_database)
        with con:
            con.rollback()
            cur = con.cursor()
            cur.execute(
                "UPDATE user SET first_name = ?, last_name = ?, role = ?, dateofbirth = ?, datestarted = ?, gender = ?, bio = ?, pictureURL = ? WHERE userID = ?",
                (_firstName, _lastName, _role, _dateOfBirth, _dateStarted, _gender, _userBio, _pictureURL, _userID))
            con.commit()
            return 'Update Successful'
    except lite.Error, e:
        return str(e)

    finally:
        cur.close()
        con.close()


# get user information from the database
def getAllUsers(_database):
    con = None
    try:
        # connect to sqlite3
        con = lite.connect(_database)
        with con:
            con.rollback()
            cur = con.cursor()
            cur.execute("SELECT * FROM user")
            con.commit()
            return cur.fetchall()
    except lite.Error, e:
        return str(e)

    finally:
        cur.close()
        con.close()

# get if user ID exists
def containsUserID(_database, _userID):
    con = None
    try:
        # connect to sqlite3
        con = lite.connect(_database)
        with con:
            con.rollback()
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE userID=? ", (_userID))
            con.commit()
            if len(cur.fetchall()) > 0:
                return True
            else:
                return False
    except lite.Error, e:
        return str(e)

    finally:
        cur.close()
        con.close()

# search user database
def queryUserDatabase(_database, _query):
    search_query = _query.rstrip().split(' ');
    con = None
    try:
        # connect to sqlite3
        con = lite.connect(_database)
        with con:
            con.rollback()
            cur = con.cursor()
            for q in search_query:
                querybuilder =  "SELECT * FROM user WHERE userID LIKE '" + q + "%'" \
                                " UNION" \
                                " SELECT * FROM user WHERE first_name LIKE '" + q + "%'" \
                                " UNION" \
                                " SELECT * FROM user WHERE last_name LIKE '" + q + "%'" \
                                " UNION" \
                                " SELECT * FROM user WHERE email LIKE '" + q + "%'"   \
                                " UNION " \
                                "SELECT * FROM user WHERE userID LIKE '%" + q + "%'" \
                                " UNION" \
                                " SELECT * FROM user WHERE first_name LIKE '%" + q + "%'" \
                                " UNION" \
                                " SELECT * FROM user WHERE last_name LIKE '%" + q + "%'" \
                                " UNION" \
                                " SELECT * FROM user WHERE email LIKE '%" + q + "%'" \
                                " UNION " \
                                 "SELECT * FROM user WHERE userID LIKE '%" + q + "'" \
                                " UNION" \
                                " SELECT * FROM user WHERE first_name LIKE '%" + q + "'" \
                                " UNION" \
                                " SELECT * FROM user WHERE last_name LIKE '%" + q + "'" \
                                " UNION" \
                                " SELECT * FROM user WHERE email LIKE '%" + q + "'" 
                cur.execute(querybuilder)
                con.commit()
            data = cur.fetchall()
            if len(data) > 0:
                return data
            return 'no results'
    except lite.Error, e:
        return str(e)
    finally:
        cur.close()
        con.close()
