from pathlib import Path
import os
from ..settings import BASE_DIR, INSTALLED_APPS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJ_DIR = Path(__file__).resolve(strict=True).parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY', 'secure_secret_key')

DEBUG = False if 'DEBUG_FALSE' in os.environ else True

HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
if any(HOSTS):
    ALLOWED_HOSTS += HOSTS

INSTALLED_APPS += [
    'survey',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    PROJ_DIR / 'static'
]

STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

FILE_UPLOAD_PERMISSIONS = 0o644

#LOGIN_URL = '/login/'
#LOGIN_REDIRECT_URL = '/'


#try:
#    # Email
#    EMAIL_HOST = os.environ['EMAIL_HOST']
#    EMAIL_PORT = os.environ['EMAIL_PORT']
#    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
#    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
#    EMAIL_USE_TLS = False
#    EMAIL_USE_SSL = True
#
#
#    # Celery
#    CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
#    CELERY_ACCEPT_CONTENT = ['json']
#    CELERY_TASK_SERIALIZER = 'json'
#except:
#    pass
