from . common import *


DEBUG = True

SECRET_KEY = 'django-insecure-3*!n+v=@2z&2a3+q@#9-%&^eigl9wk^^(vl2_omw#p$ha4mr3d'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}