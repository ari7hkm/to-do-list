import environ
from . common import *


env = environ.Env()
environ.Env.read_env()

DEBUG = True

SECRET_KEY = 'django-insecure-3*!n+v=@2z&2a3+q@#9-%&^eigl9wk^^(vl2_omw#p$ha4mr3d'

ALLOWED_HOSTS = ['web-production-3640.up.railway.app', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://web-production-3640.up.railway.app']


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': env('DATABASE_NAME'),
#         'HOST': env('DATABASE_HOST'),
#         'USER': env('DATABASE_USER'),
#         'PASSWORD': env('DATABASE_PASSWORD')
#     }
# }

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME':'db.sqlite3'
    }
}