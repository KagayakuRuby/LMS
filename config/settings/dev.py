from .base import *
from pathlib import Path
from decouple import config , csv

DEBUG = config("DEBUG",cast=bool)

ALLOWED_HOSTS +=  ["127.0.0.1","localhost"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'LMS',
        'USER':'postgres',
        'PASSWORD':'123',
        'HOST':'localhost',
        'PORT':'5432',
    }
}