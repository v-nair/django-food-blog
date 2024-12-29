from decouple import config

ENVIRONMENT = config("DJANGO_ENVIRONMENT", default="development")

if ENVIRONMENT == "production":
    # Explicit imports instead of star imports
    from .production import *  # noqa: F401,F403
elif ENVIRONMENT == "development":
    from .development import *  # noqa: F401,F403
else:
    raise ValueError("Invalid DJANGO_ENVIRONMENT. Choose 'development' or 'production'.")
