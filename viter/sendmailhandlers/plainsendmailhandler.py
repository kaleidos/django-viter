from .sendmailhandlerbase import SendmailHandlerBase
from django.core.mail import send_mail
from django.contrib.sites.models import Site
from .. import settings
from django import template

class PlainSendmailHandler(SendmailHandlerBase):
    '''Plain text Sendmail handler'''

    def send(self, invitation, **kwargs):
        '''
        Send an invitation to kwargs['email'] or invitation.email

        Generate the email text from the templates viter/email/subject.txt and
        viter/email/body.txt with \*\*kwargs and invitation in the context.
        '''
        email = kwargs.get('email', None)
        if not email:
            email = getattr(invitation, 'email', None)
        if not email:
            return False

        message = kwargs.get('message', None)

        if settings.VITER_URL_NAME:
            url = reverse(settings.VITER_URL_NAME, args=invitation.hash)
        elif settings.VITER_URL_STRING:
            url = settings.VITER_URL_STRING % { 'hash': invitation.hash }
        else:
            raise Exception('Misconfigured URL generation, define your VITER_URL_NAME or your VITER_URL_STRING')

        ctx = {'invitation': invitation}
        ctx.update(kwargs)
        ctx.update(site=Site.objects.get_current(), url=url)
        ctx = template.Context(ctx)
        
        subject_template = kwargs.pop('subject_template', 'viter/email/subject.txt')
        body_template = kwargs.pop('body_template', 'viter/email/body.txt')
        
        subject = template.loader.get_template(subject_template)
        body = template.loader.get_template(body_template)
        
        subject = subject.render(ctx)
        body = body.render(ctx)
        
        subject = ' '.join(subject.split('\n')) # No newlines in subject lines allowed
        
        return send_mail(subject, body, settings.VITER_FROM_EMAIL, [email])
