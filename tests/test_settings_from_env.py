import sys

import pytest
import pydantic


_FAKE_ATTACH = "ATTACH 'dbname=camino host=host.docker.internal' user='pharmacy_dashboard' password='super secret'"


def _clear():
    sys.modules.pop("app.config", None)
    app_package = sys.modules.get("app")
    if app_package is not None:
        vars(app_package).pop("config", None)


@pytest.fixture
def mocked_settings(monkeypatch):
    """Mock the settings for testing."""
    monkeypatch.setenv("CAMINO_ATTACH", _FAKE_ATTACH)
    monkeypatch.setenv("HTTP_PROXY", "https://mocked.proxy.url:1234")
    _clear()

    yield

    _clear()


@pytest.mark.usefixtures("mocked_settings")
def test_get_mocked_settings():
    """Test that the settings are correctly mocked."""

    from app.config import settings

    assert settings.CAMINO_ATTACH.get_secret_value() == _FAKE_ATTACH
    assert settings.HTTP_PROXY == "https://mocked.proxy.url:1234"


def test_cant_get_settings_without():
    with pytest.raises(pydantic.ValidationError):
        from app.config import settings  # noqa: F401
