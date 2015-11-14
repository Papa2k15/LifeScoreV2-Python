from dao.user_dao import user_dao
from dao.user_info_dao import user_info_dao
from dao.mission_dao import mission_dao

class dao_factory(object):
    instance = None
    
    def __init__(self):
        if self.instance is not None:
            return self.instance
        
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = dao_factory()
        return cls.instance
    
    def get_user_dao(self):
        return user_dao()

    def get_user_info_dao(self):
        return user_info_dao()
    
    def get_mission_dao(self):
        return mission_dao()