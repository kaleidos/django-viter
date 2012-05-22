from .generatorhandlerbase import GeneratorHandlerBase
from uuid import uuid4

class UUIDGeneratorHandler(GeneratorHandlerBase):
    def generate(self, **kwargs):
        return uuid4()
