import sqlite3 as sqlite

life_score_con = sqlite.connect('lifescore.db')

clear_tables_script =  """
                DELETE FROM user;
                DELETE FROM userinfo;
                DELETE FROM mission;
                DELETE FROM log;
                """

test_data_script = """ 
    /* Test data for users*/
        INSERT INTO `user` (first_name,last_name,datejoined,username,email,password) VALUES ('Gregory','Daniels','05/16/2015','Papa2k15','gldaniel@ncsu.edu','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');        
        INSERT INTO `userinfo` (bio,dateofbirth,gender,favcolor) VALUES ('LETS GO WHAT WHAT!!!!',"06/15/1993",'male','red');        
    """
    
try:
    cursor = life_score_con.cursor()
    cursor.executescript(clear_tables_script)
    cursor.executescript(test_data_script)
    life_score_con.commit()
    print "Operation complete\n"                    
except Exception, e:
    print e
finally:    
    life_score_con.close()
