class AbstractApplication:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()
