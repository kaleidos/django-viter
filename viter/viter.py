from storehandlers import storehandler
from generatorhandlers import generatorhandler
from sendmailhandlers import sendmailhandler

class Viter(object):
    '''Main interface class'''

    def invite_emails(self, emails, **kwargs):
        '''Generate and send invitations to a list of emails'''
        for email in emails:
            invitation = self.generate(email=email, **kwargs)
            self.send_by_mail(invitation, **kwargs)

    def generate(self, **kwargs):
        '''Generate an invitation'''
        hash = generatorhandler.generate(**kwargs)
        return storehandler.create(hash, **kwargs)

    def register_usage(self, hash, **kwargs):
        '''Send by mail an invitation'''
        return storehandler.register_usage(hash, **kwargs)

    def send_by_mail(self, invitation, **kwargs):
        '''Send by mail an invitation'''
        return sendmailhandler.send(invitation, **kwargs)

    def get(self, hash, **kwargs):
        '''Get an invitation object from the hash'''
        return storehandler.get(hash, **kwargs)
