class SendmailHandlerBase(object):
    def send(self, invitation, **kwargs):
        raise NotImplementedError
