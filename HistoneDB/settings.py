"""
Django settings for HistoneDB project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Set the MySQL dtabase information. If this in an NCBI machine, it will already be set as an environment variable
NCBI_database_info = {
    "name": "histdb",
    "user": "histdb",
    "password": "pass",
    "host": "localhost",
    "port": 3306,
    "SECRET_KEY": "DJANGO_SECRET_KEY"
}
NCBI_database_info.update({key.replace("NCBI_database_info_", ""): value for key, value in os.environ.iteritems() if key.startswith("NCBI_database_info")})

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = NCBI_database_info["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("HistonDB_DEBUG", True)

if not DEBUG:
    #X_FRAME_OPTIONS = "DENY"
    #CSRF_COOKIE_HTTPONLY = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    #SECURE_SSL_REDIRECT = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    #SECURE_HSTS_SECONDS = 0

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'browse',
    'djangophylocore',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'HistoneDB.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TEMPLATE_DIRS = [os.path.join(BASE_DIR, "templates"),]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

WSGI_APPLICATION = 'HistoneDB.wsgi.application'

# Database

# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': NCBI_database_info["name"],
        'USER': NCBI_database_info["user"],
        'PASSWORD': NCBI_database_info["password"],
        'HOST': NCBI_database_info["host"],
        'PORT':NCBI_database_info["port"]
    }
}

DATABASE_ENGINE="mysql"

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATIC_ROOT_AUX = os.path.join(BASE_DIR, "static")


STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
]

#MEDIA_URL = "/projects/histonedb/HistoneDB/media/"
#MEDIA_ROOT = "/web/projects/histonedb/HistoneDB/media/"

# List of finder classes that know how to find static files in
# various locations.
#STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#)
#STATIC_FINDERS = STATICFILES_FINDERS
