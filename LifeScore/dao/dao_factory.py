from dao.user_dao import user_dao
import sqlite3 as lite

class dao_factory(object):
    instance = None
    life_score_con = None
    
    def __init__(self):
        if self.instance is not None:
            return self.instance
        self.life_score_con = lite.connect('lifescore.db')
        
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = dao_factory()
        return cls.instance
    
    def get_user_dao(self):
        return user_dao(self.life_score_con)
