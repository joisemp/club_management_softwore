from . base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = []

if not DEBUG:
    ALLOWED_HOSTS += [os.environ.get('ALLOWED_HOSTS')]

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR, 'static']

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATIC_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'