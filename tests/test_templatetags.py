from django import template
from djregistry import registry
import pytest


@pytest.mark.parametrize(
    "template_string,rendered", (
        ("""{% load registry %}{{ "1"|from_registry }}""", "2"),
        ("""{% load registry %}{{ "foo"|from_registry }}""", ""),
        ("""{% load registry %}{{ "foo"|from_registry|default:"bar" }}""", "bar"),
    )
)
def test_from_registry(template_string, rendered, monkeypatch):
    monkeypatch.setattr(registry, "_registry", {
        "1": "2"
    })
    assert template.Template(template_string).render(template.Context()) == rendered
