import os
from . import common

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR =os.path.dirname( os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1tn#1tvf^=ktrpw--zr)yvu@38!g$#mbujazl#2iyo5bz@6q5v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['133.130.113.34.xip.io']


ROOT_URLCONF = 'mainHP.urls'

WSGI_APPLICATION = 'mainHP.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'main_db',
        'USER': 'kiyama',
        'PASSWORD': 'kmakm19980117',
        'HOST': 'kiyama-postgres-1.cd5xwmcuxbyt.ap-southeast-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_ROOT='/static/'
