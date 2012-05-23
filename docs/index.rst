Welcome to django-viter's documentation!
========================================

django-viter allows you to invite users to your Django application and track
the usage of the invitations.

Installation
------------

::

    pip install django-viter
    

Configuration
-------------

Add ``viter``, ``viter.storehandlers.dbstorehandler``, ``django.contrib.sites`` to your ``INSTALLED_APPS``

::

    INSTALLED_APPS = (
        'django.contrib.sites',
        'viter'
        'viter.storehandlers.dbstorehandler'
    )
    
   
Usage
-----

To invite people make use of :attr:`viter.viter.Viter.invite_emails`

::

    from viter.viter import Viter
    
    Viter.invite_emails(['foo@bar.com', 'bar@foo.com'], request.user)


You can keep track of who invites whom:

::

    from django.contrib.auth.models import User
    foo = User.objects.get(username='foo')
    invitations = foo.invitations.all()

You can keep track of who use what invitations:

::

    from viter.viter import Viter
    from django.contrib.auth.models import User

    foo_user = User.objects.get(username='foo')
    bar_user = User.objects.get(username='bar')
    invitation = foo_user.invitations.all()[0]

    viter = Viter()
    viter.register_usage(invitation, user=bar_user)

    invitation_usages = invitation.usages.all()

    bar_use_this_invitations = bar_user.invitations_used.all()
    
    
By default :attr:`viter.viter.Viter.invite_emails` will render ``viter/email/subject.txt``
and ``viter/email/body.txt`` for the email.

Settings
--------

There are a couple of editable settings

.. attribute:: VITER_STORE_HANDLER

    :Default: :class:`viter.storehandlers.dbstorehandler.DBStoreHandler`
    :type: str
    
    This indicate the Store Handler used to store the invitation objects.
    
.. attribute:: VITER_GENERATOR_HANDLER
    
    :Default: :class:`viter.generatorhandlers.uuidgeneratorhandler.UUIDGeneratorHandler`
    :type: str
    
    This indicate the Generator Handler used to generate unique ids.
    
.. attribute:: VITER_SENDMAIL_HANDLER
    
    :Default: :class:`viter.sendmailhandlers.plainsendmailhandler.PlainSendmailHandler`
    :type: str
    
    This indicate the Sendmail Handler used to construct and send invitation emails.
    
.. attribute:: VITER_URL_NAME

    :Default: ``''``
    
    The url name to generate the emails urls with reverse(VITER_URL_NAME, args=hash)
    If not defined viter will use the VITER_URL_STRING.
    
.. attribute:: VITER_URL_STRING

    :Default: ``'/?%(hash)s'``
    
    The url string to generate the emails urls with VITER_URL_STRING % { hash: hash }.
    
.. attribute:: VITER_FROM_EMAIL

    :Default: ``settings.DEFAULT_FROM_EMAIL``
    
    The email address used to send invites from
    
API
---

.. toctree::
    :maxdepth: 3
    
    viter

Made by `Kaleidos <http://www.kaleidos.net/>`_. 
