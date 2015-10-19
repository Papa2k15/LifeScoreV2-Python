'''
Created on Oct 18, 2015

@author: Owner
'''

class user_bean(object):
    '''
    classdocs
    '''

    def __init__(self, first_name, last_name, email, username, password, *user_id):
        '''
        Constructor
        '''
        if not user_id:
            self.user_id = None
        else:
            self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password= password
        
        