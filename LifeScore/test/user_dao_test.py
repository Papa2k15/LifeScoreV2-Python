'''
Created on Oct 18, 2015

@author: Owner
'''
import unittest
import sqlite3 as lite
from beans.user_bean import user_bean
from dao.dao_factory import dao_factory

life_score_test_database = 'lifescore_test.db'
con = None

class user_dao_tests(unittest.TestCase):
    
    global factory 
    global example_user_1

    def setUp(self):
        global factory 
        global example_user_1
        factory = dao_factory.get_instance(life_score_test_database)
        example_user_1 = user_bean("Gregory","Daniels","gldaniel@ncsu.edu", "Papa2k15", "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8")
        try:
            con = lite.connect(life_score_test_database)
            with con:
                cur = con.cursor()
                cur.executescript(
                    """
                    DROP TABLE IF EXISTS "user";

                    CREATE TABLE "user" (
                    `userID`    INTEGER UNIQUE,
                    `name`    TEXT NOT NULL,
                    `username`    TEXT NOT NULL,
                    `email`    TEXT NOT NULL,
                    `password`    TEXT NOT NULL,
                    PRIMARY KEY(userID)
                    )""")
                con.commit()
        except lite.Error, e:
            return str(e)
        finally:
            if con:
                con.close()

    def tearDown(self):
        try:
            con = lite.connect(life_score_test_database)
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS user")
        except lite.Error, e:
            return str(e)
        finally:
            if con:
                con.close()


    def test_add_new_user(self):
        global factory
        global example_user_1
        print factory.get_user_dao().get_all_users()
        #self.assertEquals(len(factory.get_user_dao().get_all_users()), 0)

if __name__ == "__main__":
    unittest.main()