from .generatorhandlerbase import GeneratorHandlerBase

class NoGeneratorHandler(GeneratorHandlerBase):
    def generate(self, **kwargs):
        return None
