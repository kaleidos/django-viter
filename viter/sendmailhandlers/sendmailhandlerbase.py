class SendmailHandlerBase(object):
    '''Abstract class for Sendmail Handlers'''

    def send(self, invitation, **kwargs):
        '''Abstract method'''
        raise NotImplementedError
