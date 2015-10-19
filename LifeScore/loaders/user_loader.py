'''
Created on Oct 18, 2015

@author: Owner
'''
from beans.user_bean import user_bean

class user_loader(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
    def load_single(self, cursor):
        single_user_data = cursor.fetchone()
        return user_bean(single_user_data[1],single_user_data[2], single_user_data[3], single_user_data[4], single_user_data[5],single_user_data[0])
    
    def load_list(self, cursor):
        multiple_user_data = cursor.fetchall()
        user_list = []
        for user in multiple_user_data:
            user_list.append(user_bean(user[1], user[2], user[3], user[4],user[5],user[0]))
        return user_list