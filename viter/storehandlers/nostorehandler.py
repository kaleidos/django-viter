from .storehandlerbase import StoreHandlerBase

class NoStoreHandler(StoreHandlerBase):
    def create(self, uniq_id, **kwargs):
        return None

    def register_usage(self, uniq_id, **kwargs):
        return True

    def get(self, uniq_id, **kwargs):
        return None
