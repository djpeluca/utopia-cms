# -*- coding: utf-8 -*-
from datetime import datetime


INTERNAL_IPS = ('127.0.0.1', '0.0.0.0', '*')
REMOTE_ADDR = ('*')

DEBUG = True
TEMPLATE_DEBUG = DEBUG
REMOVE_WWW = not DEBUG
SEND_BROKEN_LINK_EMAILS = False
RESTRICT_ACCESS = False
RESTRICT_ACCESS_LOGIN_URL = '/acceso-beep/'
SECRET_KEY = ''

# Site settings
CLOSED_SITE = False
SITE_DOMAIN = "yoogle.com"
SESSION_COOKIE_DOMAIN = "." + SITE_DOMAIN
ALLOWED_HOSTS = [SESSION_COOKIE_DOMAIN]

COMPRESS_OFFLINE = False
COMPRESS_ENABLED = True

if CLOSED_SITE or RESTRICT_ACCESS:
    from settings import INSTALLED_APPS, MIDDLEWARE_CLASSES
    INSTALLED_APPS += ('closed_site', )
    MIDDLEWARE_CLASSES = (
        'closed_site.middleware.ClosedSiteMiddleware',
        'closed_site.middleware.RestrictedAccessMiddleware',
    ) + MIDDLEWARE_CLASSES

ADMINS = (
    (u'Admin', 'admin@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'utopiacms',
        'USER': 'utopiacms_user',
        'PASSWORD': 'password',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    },
}

TIME_ZONE = 'America/Montevideo'

USE_I18N = True

DATE_FORMAT = 'l j de F de Y'
TIME_FORMAT = 'H:i:s'
DATETIME_FORMAT = '%s %s' % (DATE_FORMAT, TIME_FORMAT)
SHORT_DATE_FORMAT = 'd/m/Y'

STATICFILES_DIRS = (
    '/home/user/utopia-cms/static',
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

LOGIN_URL = '/usuarios/entrar/'
LOGOUT_URL = '/usuarios/salir/'
SIGNUP_URL = '/usuarios/registro/'
LOGIN_REDIRECT_URL = '/'

# EMAIL
EMAIL_SUBJECT_PREFIX = u'[cms] '
DEFAULT_FROM_EMAIL = 'cms dev <cms@example.com>'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 2500
EMAIL_CONFIRMATION_TIMEOUT_DAYS = 3

SERVER_EMAIL = DEFAULT_FROM_EMAIL

SENDNEWSLETTER_LOGFILE = '/home/user/utopia-cms-data/sendnewsletter/%s-%s.log'

# TODO: remove this commented setting if not useful
# SOUTH_DATABASE_ADAPTERS = {
#     'default': "south.db.mysql"
# }

LAST_OLD_DAY = datetime(2013, 6, 15)
EMAIL_EDITION_NUMBER_OFFSET = 0

# Google tag manager
GTM_CONTAINER_ID = ''
GTM_AMP_CONTAINER_ID = ''

# Recaptcha
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
SUBSCRIPTION_CAPTCHA_DEFAULT_COUNTRY = ''  # 2-char (in caps) country iso code
SUBSCRIPTION_CAPTCHA_COUNTRIES_IGNORED = [SUBSCRIPTION_CAPTCHA_DEFAULT_COUNTRY]
