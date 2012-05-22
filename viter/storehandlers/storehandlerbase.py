class StoreHandlerBase(object):
    '''Abstract class for Store Handlers'''

    def create(self, hash, **kwargs):
        '''Abstract method'''
        raise NotImplementedError

    def register_usage(self, hash, **kwargs):
        '''Abstract method'''
        raise NotImplementedError

    def get(self, hash, **kwargs):
        '''Abstract method'''
        raise NotImplementedError
