from django.conf import settings

VITER_STORE_HANDLER = getattr(settings, 'VITER_STORE_HANDLER', 'viter.storehandlers.dbstorehandler.DBStoreHandler')
VITER_GENERATOR_HANDLER = getattr(settings, 'VITER_GENERATOR_HANDLER', 'viter.generatorhandlers.uuidgeneratorhandler.UUIDGeneratorHandler')
VITER_SENDMAIL_HANDLER = getattr(settings, 'VITER_SENDMAIL_HANDLER', 'viter.sendmailhandlers.plainsendmailhandler.PlainSendmailHandler')
VITER_URL_NAME = getattr(settings, 'VITER_URL_NAME', '')
VITER_URL_STRING = getattr(settings, 'VITER_URL_STRING', '/?%(hash)s')
VITER_FROM_EMAIL = getattr(settings, 'VITER_FROM_EMAIL', settings.DEFAULT_FROM_EMAIL)
