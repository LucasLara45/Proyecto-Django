from .settings import *

DEBUG = True
ALLOWED_HOSTS = []
STATIC_ROOT = None
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}