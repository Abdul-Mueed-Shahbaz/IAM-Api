from .base import *

DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "iam-api",
        "USER": env.str("username"),
        "PASSWORD": env.str("password"),
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = [
    # "REFRESHTOKEN",
    # "content-type"
]
