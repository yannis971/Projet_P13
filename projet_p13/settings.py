"""
Module : settings.py
Modified by : Yannis Saliniere
"""
import os
from pathlib import Path

import environ
import sentry_sdk
from django.core.management.utils import get_random_secret_key
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DJANGO_SERVER_TYPE = os.getenv(key="DJANGO_SERVER_TYPE", default="local")

# Application definition

INSTALLED_APPS = [
    "oc_lettings_site.apps.OCLettingsSiteConfig",
    "lettings.apps.LettingsConfig",
    "profiles.apps.ProfilesConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "projet_p13.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "projet_p13.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "oc-lettings-site.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Clear prev config
LOGGING_CONFIG = None

# Get loglevel from env
LOGLEVEL = os.getenv("DJANGO_LOGLEVEL", "info").upper()

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d \
            %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
    },
    "loggers": {
        "": {
            "level": LOGLEVEL,
            "handlers": [
                "console",
            ],
        },
    },
}


django_server_type = os.getenv(key="DJANGO_SERVER_TYPE", default=None)

if django_server_type == "production":
    from os import getenv as env

    import dj_database_url

    # Heroku: Update database configuration from $DATABASE_URL.
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES["default"].update(db_from_env)
else:
    # Take environment variables from .env file
    env = environ.Env()
    environ.Env.read_env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default=get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG", default=False)

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS", default="*").split(",")

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default=None)
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default=None)
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", default=None)

AMAZON_STORAGE = bool(
    AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and AWS_STORAGE_BUCKET_NAME
)

# Stockage des ressources statiques sur Amazon
if AMAZON_STORAGE and django_server_type == "production":
    # Boto3
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }
    AWS_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"
else:
    STATIC_URL = "/static/"

STATIC_ROOT = Path.joinpath(BASE_DIR, "static")
STATICFILES_DIR = Path.joinpath(BASE_DIR, "static")

# Sentry
sentry_sdk.init(
    dsn=env("SENTRY_SDK_DSN", default=None),
    integrations=[DjangoIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=env("SENTRY_TRACES_SAMPLE_RATE", default=1.0),
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
