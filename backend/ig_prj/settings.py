"""
Django settings for ig_prj project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Load environment variables
load_dotenv()
env = os.environ

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '20.121.118.165',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # own
    'post',
    'crispy_forms',
    'authy',
    'comment',
    'directs',
    'notification',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ig_prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ig_prj.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.get('AZDB_NAME'),
        'USER': env.get('AZDB_USER'),
        'PASSWORD': env.get('AZDB_PASS'),
        'HOST': env.get('AZDB_HOST'),
        'PORT': env.get('AZDB_PORT'),
    }
}

LOGGING = {
    "version": 1,  # the dictConfig format version
    "disable_existing_loggers": False,  # retain the default loggers
    "formatters": {
        "verbose": {
            "format": "{name} {levelname} {asctime} {module} {process:d} {thread:d} "
                      "{message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "debug_file": {
            "class": "logging.FileHandler",
            "filename": "logs/debug.log",
            "level": "DEBUG",
            "formatter": "verbose",
        },
        "info_file": {
            "class": "logging.FileHandler",
            "filename": "logs/info.log",
            "level": "INFO",
            "formatter": "verbose",
        },
        "warning_file": {
            "class": "logging.FileHandler",
            "filename": "logs/warning.log",
            "level": "WARNING",
            "formatter": "verbose",
        },
        "error_file": {
            "class": "logging.FileHandler",
            "filename": "logs/error.log",
            "level": "ERROR",
            "formatter": "verbose",
        },
        "critical_file": {
            "class": "logging.FileHandler",
            "filename": "logs/critical.log",
            "level": "CRITICAL",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["debug_file", "info_file", "warning_file", "error_file",
                         "critical_file"],
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

USE_TZ = True

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'index'

LOGOUT_REDIRECT_URL = 'sign-in'

LOGIN_URL = 'sign-in'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

APPEND_SLASH = False

# CSRF COOKIE SETTINGS
CSRF_COOKIE_DOMAIN = ''
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_MASKED = False
CSRF_COOKIE_PATH = '/cookies/'
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1',
    'http://localhost'
]


# CSRF SESSIONS SETTINGS
# CSRF_USE_SESSIONS = True
# SESSION_COOKIE_HTTPONLY = False
# SESSION_COOKIE_PATH = '/sessions/'
# SESSION_COOKIE_SAMESITE = 'Lax'
# SESSION_COOKIE_SECURE = False
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
