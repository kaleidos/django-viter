class GeneratorHandlerBase(object):
    '''Abstract class for Generator Handlers'''

    def generate(self, **kwargs):
        '''Abstract method'''
        raise NotImplementedError
