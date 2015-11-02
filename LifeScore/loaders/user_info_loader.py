'''
Created on Oct 18, 2015

@author: Owner
'''
from beans.user_info_bean import user_info_bean

class user_info_loader(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
    def load_single(self, cursor):
        single_user_info_data = cursor.fetchone()
        if single_user_info_data != None:
            return user_info_bean(single_user_info_data[1],single_user_info_data[0])
        return single_user_info_data