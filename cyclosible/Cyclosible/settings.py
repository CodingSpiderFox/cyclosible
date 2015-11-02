"""
Django settings for Cyclosible project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'djcelery',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'guardian',
    'cyclosible.playbook',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'ws4redis',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
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

ROOT_URLCONF = 'cyclosible.Cyclosible.urls'

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

SWAGGER_SETTINGS = {
    'is_authenticated': True,
    'is_superuser': False,
    'permission_denied_handler': 'cyclosible.Cyclosible.views.permission_denied_handler',
}

WSGI_APPLICATION = 'ws4redis.django_runserver.application'
WEBSOCKET_URL = '/ws/'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

ANONYMOUS_USER_ID = None

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

"""
##############################################################################################
#######                           USER CONFIGURATION HERE                              #######
##############################################################################################
"""

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

WS4REDIS_SUBSCRIBER = 'cyclosible.Cyclosible.websocket.WebSocketSubscriber'
WS4REDIS_PREFIX = 'ws'
WS4REDIS_EXPIRE = 7200
WS4REDIS_CONNECTION = {
    'host': 'localhost',
    'port': 6379,
    'db': 1,
}

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'Europe/Paris'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'll=1_7y5i4e!5)@g+25ouhhz2kru6d=15twq5c)faerhj5x^@9'

# Trailing slash is needed here
PLAYBOOK_PATH = "/home/<playbook-path>/"

STORAGE_ENABLED = ['s3']

# Can be 'password', 'file' or 'hashicorp'.
# The hashicorp plugin will request the password in hashicorp's vault
# Let this variable to None to disable vault password
# Uncomment VAULT_* variables to configure the plugins
# As it's a python file, you can also use os.environ to get the
# value from your environment

VAULT_ENABLED = None
# VAULT_PASSWORD = "XXXXXXXX"
# VAULT_FILE = "/home/<vault_password_path>"
# VAULT_HASHICORP = {
#     'scheme': 'https',
#     'host': 'vault.company.com',
#     'port': 8200,
#     'token': 'xxxxxxxxxxxxxxxxx',
#     'secret_path': 'cycloid/ansible',
#     'secret_field': 'value'
# }

S3_BUCKET = "cycloid-cyclosible"
S3_ACCESS_KEY = "XXXXXXXXXXX"
S3_SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

if 'CYCLOSIBLE_CONFIG' in os.environ:
    execfile(os.environ['CYCLOSIBLE_CONFIG'])
