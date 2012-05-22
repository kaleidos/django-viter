from .sendmailhandlerbase import SendmailHandlerBase

class NoSendmailHandler(SendmailHandlerBase):
    def send(self, invitation, **kwargs):
        return True
