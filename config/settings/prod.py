# SECURITY WARNING: don't run with debug turned on in production!
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*.joway.wang']


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
