import os
from .common import *


SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

STATICFILES_STORAGE = "config.storages.StaticAzureStorage"
DEFAULT_FILE_STORAGE = "config.storages.MediaAzureStorage"

# AZURE_ACCOUNT_NAME = os.environ["AZURE_ACCOUNT_NAME"]
# AZURE_ACCOUNT_KEY = os.environ["AZURE_ACCOUNT_KEY"]

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("DB_NAME", "postgres"),
        "USER": os.environ["DB_USER"],  # Admin username
        "HOST": os.environ["DB_HOST"],  # Server name
        "PASSWORD": os.environ["DB_PASSWORD"],
    }
}

CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS", "").split(",")  # CORS 설정

LOGGING = {
    "version": 1,
    "disable_exiting_loggers": False,
    "handlers": {
        "console": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "ERROR",
        },
    },
}