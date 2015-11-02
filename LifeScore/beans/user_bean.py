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
            self.user_id = int(user_id[0])
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.email = str(email)
        self.username = str(username)
        self.password= str(password)
        
        