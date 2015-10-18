import sqlite3 as sqlite

life_score_con = sqlite.connect('lifescore.db')

clear_tables_script =  """
                DELETE FROM user;
                """

test_data_script = """ 
    /* Test data for users*/
        INSERT INTO `user` (userID,first_name,last_name,role,email,dateofbirth,gender,datestarted,bio,pictureURL) VALUES (1,'Bob','Tables','engineer','bob@email.com','B',NULL,NULL,'Bob is a native of Mexico City and has lived in Portland, Oregon since 1996. Since 2008, He has been District Executive for Hispanic Outreach and responsible for the Soccer and Scouting program at the Boy Scouts of America in Portland. His bi-cultural background and focus on community collaboration has led him to a number of volunteer opportunities and community leadership roles. Rolando received his Bachelor of Science in Communications at Oklahoma Christian University and a Masters in Management and Organizational Leadership at Warner Pacific College in Portland, Oregon.','/static/images/Bob B Tables.jpg');        
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
