from decouple import config
from .base import *  # noqa: F401,F403

DEBUG = True
ALLOWED_HOSTS = ["*"]

SECRET_KEY = config("DJANGO_SECRET_KEY", default="dev-key")

# CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = [
    "https://localhost",
    "https://127.0.0.1",
    "http://localhost",
    "http://127.0.0.1",
]

# Recognize the X-Forwarded-Proto header to determine if the request is secure
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB", default="foodie_dev"),
        "USER": config("POSTGRES_USER", default="foodie_user"),
        "PASSWORD": config("POSTGRES_PASSWORD", default="supersecretpassword"),
        "HOST": config("DATABASE_HOST", default="db"),
        "PORT": config("DATABASE_PORT", default="5432"),
    }
}

# Update LOGGING settings
LOGGING["handlers"]["console"]["formatter"] = "verbose"  # noqa: F405
LOGGING["root"]["level"] = "DEBUG"  # noqa: F405
