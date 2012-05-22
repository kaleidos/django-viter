from .. import settings
from django.utils.importlib import import_module

__all__ = ('sendmailhandler',)

module_name = ".".join(settings.VITER_SENDMAIL_HANDLER.split(".")[0:-1])
class_name = settings.VITER_SENDMAIL_HANDLER.split(".")[-1]
sendmailhandler = getattr(import_module(module_name), class_name)()
