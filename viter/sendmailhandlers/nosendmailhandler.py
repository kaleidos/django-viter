from .sendmailhandlerbase import SendmailHandlerBase

class NoSendmailHandler(SendmailHandlerBase):
    '''Fake Sendmail Handler, do nothing'''

    def send(self, invitation, **kwargs):
        '''do nothing and return True'''
        return True
