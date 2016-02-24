__version__ = '0.1.0'


__all__ = (
    "registry",
)


class Registry(object):

    _registry = None

    @staticmethod
    def _flatten_dict(nested):
        flat = {}
        for key, value in nested.items():
            if isinstance(value, dict):
                flat.update(("{}.{}".format(key, k), v) for k, v in Registry._flatten_dict(value).items())
            else:
                flat[key] = value
        return flat

    @property
    def registry(self):
        if self._registry is None:
            from django.conf import settings
            self._registry = self._flatten_dict(getattr(settings, "REGISTRY", {}))
        return self._registry

    def get(self, key, default=None):
        return self.registry.get(key, default)

    def __getitem__(self, key):
        return self.registry[key]


registry = Registry()
