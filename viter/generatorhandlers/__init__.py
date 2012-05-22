from .. import settings
from django.utils.importlib import import_module

__all__ = ('generatorhandler',)

module_name = ".".join(settings.VITER_GENERATOR_HANDLER.split(".")[0:-1])
class_name = settings.VITER_GENERATOR_HANDLER.split(".")[-1]
generatorhandler = getattr(import_module(module_name), class_name)()
