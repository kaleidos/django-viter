from storehandlers import storehandler
from generatorhandlers import generatorhandler
from sendmailhandlers import sendmailhandler

class Viter(object):
    def invite_emails(self, emails, **kwargs):
        for email in emails:
            invitation = self.generate(email=email, **kwargs)
            self.send_by_mail(invitation, **kwargs)

    def generate(self, **kwargs):
        hash = generatorhandler.generate(**kwargs)
        return storehandler.create(hash, **kwargs)

    def register_usage(self, hash, **kwargs):
        return storehandler.register_usage(hash, **kwargs)

    def send_by_mail(self, invitation, **kwargs):
        return sendmailhandler.send(invitation, **kwargs)

    def get(self, hash, **kwargs):
        return storehandler.get(hash, **kwargs)
