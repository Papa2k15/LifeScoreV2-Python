import sqlite3 as sqlite

life_score_con = sqlite.connect('lifescore.db')

clear_tables_script =  """
                DELETE FROM user;
                """

test_data_script = """ 
    /* Test data for users*/
        INSERT INTO `user` (userID,name,username,email,password) VALUES (1,'Gregory Daniels','Papa2k15','gldaniel@ncsu.edu','5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');        
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
