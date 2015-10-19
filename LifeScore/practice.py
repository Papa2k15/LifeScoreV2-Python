'''
Created on Oct 18, 2015

@author: Owner
'''

class user_bean(object):
    '''
    classdocs
    '''

    def __init__(self, name, email, username, password, *user_id):
        '''
        Constructor
        '''
        if not user_id:
            self.user_id = None
        else:
            self.user_id = user_id[0]
        self.name = name
        self.email = email
        self.username = username
        self.password= password
        