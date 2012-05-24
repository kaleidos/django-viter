from .generatorhandlerbase import GeneratorHandlerBase
from uuid import uuid4

class UUIDGeneratorHandler(GeneratorHandlerBase):
    '''UUID based Generator handler'''

    def generate(self, **kwargs):
        '''return a new invitation hash generated with uuid4'''
        return unicode(uuid4())
