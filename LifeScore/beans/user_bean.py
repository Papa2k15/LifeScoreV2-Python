'''
Created on Oct 18, 2015

@author: Owner
'''

class user_bean(object):
    '''
    classdocs
    '''

    def __init__(self, user_id, name, email, username, password):
        '''
        Constructor
        '''
        self.user_id = user_id
        self.name = name
        self.email = email
        self.username = username
        self.password= password
        
        