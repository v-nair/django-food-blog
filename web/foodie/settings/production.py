from decouple import config
from .base import *  # noqa: F401,F403

DEBUG = False
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="your-domain.com").split(
    ","
)  # noqa: E501

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB", default="foodie_prod"),
        "USER": config("POSTGRES_USER", default="foodie_prod_user"),
        "PASSWORD": config(
            "POSTGRES_PASSWORD", default="prod_secure_password"
        ),  # noqa: E501
        "HOST": config("DATABASE_HOST", default="prod-db-host"),
        "PORT": config("DATABASE_PORT", default="5432"),
    }
}

# SECRET_KEY = open('/run/secrets/django_secret_key').read().strip()
SECRET_KEY = config("DJANGO_SECRET_KEY", default="dev-key")

# Security settings for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Update LOGGING settings
LOGGING["handlers"]["file"] = {  # noqa: F405
    "level": "WARNING",
    "class": "logging.FileHandler",
    "filename": BASE_DIR / "logs/foodie.log",  # noqa: F405
    "formatter": "verbose",
}

LOGGING["root"]["handlers"].append("file")  # noqa: F405
LOGGING["root"]["level"] = "INFO"  # noqa: F405
