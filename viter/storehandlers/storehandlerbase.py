class StoreHandlerBase(object):
    def create(self, uniq_id, **kwargs):
        raise NotImplementedError

    def register_usage(self, uniq_id, **kwargs):
        raise NotImplementedError

    def get(self, uniq_id, **kwargs):
        raise NotImplementedError
