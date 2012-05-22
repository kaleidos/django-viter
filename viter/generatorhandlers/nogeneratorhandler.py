from .generatorhandlerbase import GeneratorHandlerBase

class NoGeneratorHandler(GeneratorHandlerBase):
    '''Fake Generator Handler, do nothing'''

    def generate(self, **kwargs):
        '''do nothing and return None'''
        return None
