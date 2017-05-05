"""
Django settings for purelight project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xfp3jfyhme8q9#n=rzm8svf22_g(#m^8$(t2jdwg=@eec0dwf_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Absolute paths for where the project and templates are stored.
ABS_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
ABS_TEMPLATES_PATH = '%s/purelight_web/templates' % ABS_PROJECT_ROOT

# add root directory to PYTHONPATH
if ABS_PROJECT_ROOT not in sys.path:
    sys.path.insert(0, ABS_PROJECT_ROOT)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_jinja',
    'purelight',
    'purelight_api',
    'purelight_web',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'purelight.urls'

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ABS_TEMPLATES_PATH],
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

STATICFILES_DIRS = (
    '/home/sakith/Projects/PureLight/purelight/purelight/purelight_web/templates',
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    )


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}



WSGI_APPLICATION = 'purelight.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

import os
if (os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or
    os.getenv('SETTINGS_MODE') == 'prod'):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DATABASES = {
        'default': {
            'ENGINE': 'google.appengine.ext.django.backends.rdbms',
            'INSTANCE': 'purelight-165309:us-central1:purelight-mysqldb',
            'NAME': 'purelightDB',
            'USER': 'root',
            'PASSWORD': '1234',
        }
    }
else:
    # Running in development, so use a local MySQL database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'root',
            'PASSWORD': '123',
            'HOST': '127.0.0.1',
            'NAME': 'purelightDB',
            'PORT' : '3306',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# List of finder classes that know how to find static files in various
# locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_ROOT = '%s/static' % ABS_PROJECT_ROOT
# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = '%s/media' % ABS_PROJECT_ROOT

# The URL that handles the media, static, etc.
STATIC_URL = '/static/'
MEDIA_URL = STATIC_URL + 'media/'

# THE REST IS PRETTY MUCH DEFAULT

# Additional locations of static files
STATICFILES_DIRS = (
    'purelight_web/static',
)