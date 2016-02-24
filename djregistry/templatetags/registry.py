from django.template import Library
from djregistry import registry


register = Library()


@register.filter
def from_registry(key):
    return registry.get(key, "")
