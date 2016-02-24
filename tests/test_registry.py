from djregistry import registry
import pretend
import pytest


@pytest.fixture
def clean_registry_cache():
    registry._registry = None


def test_flatten_dict():
    # noinspection PyProtectedMember
    assert registry._flatten_dict({
        "1": "2",
        "3": {
            "4": "5"
        }
    }) == {
       "1": "2",
       "3.4": "5",
    }


# noinspection PyUnusedLocal,PyShadowingNames
def test_registry_property(clean_registry_cache, monkeypatch):
    monkeypatch.setattr("django.conf.settings", pretend.stub(REGISTRY={
        "1": "2",
        "3": {
            "4": "5"
        }
    }))
    assert registry.registry == {
        "1": "2",
        "3.4": "5",
    }


# noinspection PyUnusedLocal,PyShadowingNames
def test_registry_property_no_settings(clean_registry_cache, monkeypatch):
    monkeypatch.setattr("django.conf.settings", pretend.stub())
    assert registry.registry == {}


# noinspection PyUnusedLocal,PyShadowingNames
def test_get(clean_registry_cache, monkeypatch):
    monkeypatch.setattr(registry, "_registry", {
        "1": "2",
        "3.4": "5",
    })

    assert registry.get("1") == "2"
    assert registry.get("1", "foo") == "2"
    assert registry.get("3.4") == "5"
    assert registry.get("foo") is None
    assert registry.get("foo", "bar") == "bar"


# noinspection PyUnusedLocal,PyShadowingNames
def test_getitem(clean_registry_cache, monkeypatch):
    monkeypatch.setattr(registry, "_registry", {
        "1": "2",
        "3.4": "5",
    })

    assert registry["1"] == "2"
    assert registry["3.4"] == "5"

    with pytest.raises(KeyError):
        # noinspection PyStatementEffect
        registry["foo"]
