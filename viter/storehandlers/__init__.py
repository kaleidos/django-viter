from .. import settings
from django.utils.importlib import import_module

__all__ = ('storehandler',)

module_name = ".".join(settings.VITER_STORE_HANDLER.split(".")[0:-1])
class_name = settings.VITER_STORE_HANDLER.split(".")[-1]
storehandler = getattr(import_module(module_name), class_name)()
