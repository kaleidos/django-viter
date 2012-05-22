from ..storehandlerbase import StoreHandlerBase
from .models import *

class DBStoreHandler(StoreHandlerBase):
    def create(self, uniq_id, **kwargs):
        invitation = Invitation.objects.create(
                hash = uniq_id,
                email = kwargs.get('email', None),
                inviter = kwargs.get('inviter', None)
        )
        return invitation

    def register_usage(self, uniq_id, **kwargs):
        try:
            InvitationUsage.objects.create(
                    invitation = Invitation.objects.get(hash=uniq_id),
                    user = kwargs.get('user', None)
            )
        except Invitation.DoesNotExist:
            return False
        return True

    def get(self, uniq_id, **kwargs):
        try:
            invitation = Invitation.objects.get(hash=uniq_id)
        except Invitation.DoesNotExist:
            return None
        return invitation
