'''
Created on Oct 18, 2015

@author: Owner
'''

class user_info_bean(object):
    '''
    classdocs
    '''

    def __init__(self, bio, *user_id):
        '''
        Constructor
        '''
        if not user_id:
            self.user_id = None
        else:
            self.user_id = user_id
        self.bio = bio
        
        