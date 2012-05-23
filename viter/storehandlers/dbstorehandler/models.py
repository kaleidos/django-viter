from django.db import models
from django.contrib.auth.models import User

class Invitation(models.Model):
    hash = models.CharField(max_length=255, unique=True)
    email = models.EmailField(null=True, blank=True)
    inviter = models.ForeignKey(User, null=True, blank=True, related_name='invitations')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'viter'

    def __unicode__(self):
        return self.hash

class InvitationUsage(models.Model):
    invitation = models.ForeignKey('Invitation', null=False, blank=False, related_name='usages')
    user = models.ForeignKey(User, null=True, blank=True, related_name='invitations_used')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'viter'

    def __unicode__(self):
        return unicode(self.invitation)+u":"+unicode(self.user.email)
