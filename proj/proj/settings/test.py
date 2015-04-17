from __future__ import absolute_import

from .base import *


# or make this False and add ALLOWED_HOSTS
DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "proj",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "",
        "PORT": "",
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
