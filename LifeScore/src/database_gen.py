import sqlite3 as sqlite

#Only works if BDex database file has been removed.
life_score_con = sqlite.connect('lifescore.db')

tables_script = """

    DROP TABLE IF EXISTS "user";
    DROP TABLE IF EXISTS "log";
     
    CREATE TABLE "user" (
    `userID`    INTEGER UNIQUE,
    `first_name`    TEXT NOT NULL,
    `last_name`    TEXT NOT NULL,
    `username`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `password`    TEXT NOT NULL,
    PRIMARY KEY(userID)
    );

    CREATE TABLE `log` (
        `transactionID`    INTEGER UNIQUE,
        `userID`    INTEGER NOT NULL,
        `description`    TEXT NOT NULL,
        `date`    TEXT NOT NULL,
        `time`    TEXT NOT NULL,
        `code`    INTEGER NOT NULL,
        PRIMARY KEY(transactionID)
    );
    """

try:
    cursor = life_score_con.cursor()
    cursor.executescript(tables_script)
    life_score_con.commit()
    print "Operation complete\n"                    
except Exception, e:
    print "Something went wrong:"
    print e
finally:    
    life_score_con.close()
