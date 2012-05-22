from .storehandlerbase import StoreHandlerBase

class NoStoreHandler(StoreHandlerBase):
    '''Fake Store Handler, do nothing'''

    def create(self, hash, **kwargs):
        '''do nothing and return None'''
        return None

    def register_usage(self, hash, **kwargs):
        '''do nothing and return True'''
        return True

    def get(self, hash, **kwargs):
        '''do nothing and return None'''
        return None
