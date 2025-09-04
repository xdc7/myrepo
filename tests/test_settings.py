import os

from django.conf import settings


def test_dev_settings_module_env() -> None:
    assert os.environ.get("DJANGO_SETTINGS_MODULE") == "project.settings.dev"


def test_root_urlconf_is_project_urls() -> None:
    assert settings.ROOT_URLCONF == "project.urls"
