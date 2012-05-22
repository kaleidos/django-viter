from ..storehandlerbase import StoreHandlerBase
from .models import *

class DBStoreHandler(StoreHandlerBase):
    '''DB Store Handler, store the data in django models'''

    def create(self, hash, **kwargs):
        '''Create a new invitation object'''
        invitation = Invitation.objects.create(
                hash = hash,
                email = kwargs.get('email', None),
                inviter = kwargs.get('inviter', None)
        )
        return invitation

    def register_usage(self, hash, **kwargs):
        '''Register the usage of an invitation'''
        try:
            InvitationUsage.objects.create(
                    invitation = Invitation.objects.get(hash=hash),
                    user = kwargs.get('user', None)
            )
        except Invitation.DoesNotExist:
            return False
        return True

    def get(self, hash, **kwargs):
        '''Get an invitation from the hash'''
        try:
            invitation = Invitation.objects.get(hash=hash)
        except Invitation.DoesNotExist:
            return None
        return invitation
