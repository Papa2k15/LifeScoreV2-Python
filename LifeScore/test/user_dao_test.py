'''
Created on Oct 18, 2015

@author: Owner
'''
import unittest
import sqlite3 as lite
from beans.user_bean import user_bean


life_score_test_database = 'lifescore_test.db'
con = None

class user_dao_tests(unittest.TestCase):

    example_user_1 = user_bean("2", "Gregory", "gldaniel@ncsu.edu", "Papa2k15", "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8")

    def setUp(self):
        try:
            con = lite.connect(life_score_test_database)
            with con:
                cur = con.cursor()
                cur.execute(
                    """
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
        user_da


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_add_new_user']
    unittest.main()