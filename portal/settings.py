# -*- coding: utf-8 -*-
import sys
from os.path import abspath, basename, dirname, join, realpath
from datetime import datetime
import mimetypes
from freezegun import freeze_time

from django.contrib.messages import constants as messages


LAST_OLD_DAY = datetime(2014, 7, 22)
FIRST_DAY = datetime(2009, 8, 1)

PROJECT_ABSOLUTE_DIR = dirname(abspath(__file__))
PROJECT_NAME = basename(PROJECT_ABSOLUTE_DIR)
APPS_DIR = join(PROJECT_ABSOLUTE_DIR, "apps")
if APPS_DIR not in sys.path:
    sys.path.insert(0, APPS_DIR)

SITE_ROOT = dirname(realpath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = '%s/static/' % SITE_ROOT
SITE_DOMAIN = 'example.com'
URL_SCHEME = "https"
DEFAULT_URL_SCHEME = URL_SCHEME

# django-mobile
FLAVOURS = ('full', 'mobile', 'amp')
FLAVOURS_GET_PARAMETER = u'display'
FLAVOURS_COOKIE_SECURE = True

# Multi sub-domain secure cookie
SESSION_COOKIE_DOMAIN = ".ladiaria.com.uy"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_AGE = 2592000  # 30 days
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SAMESITE_FORCE_ALL = True
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

AMP_DEBUG = False
RAW_SQL_DEBUG = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

INSTALLED_APPS = (
    'django_mobile',
    'django.contrib.staticfiles',
    'admin_shortcuts',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'background_task',
    'subdomains',
    'audiologue',
    'tagging',
    'core.config.CoreConfig',
    'core.attachments',
    'django_extensions',
    'generator',
    'memcached',
    'shoutbox',
    'thedaily',
    'videologue',
    'short',
    'adzone',
    'exchange',
    'faq',
    'captcha',
    'photologue',
    'sortedm2m',
    'photologue_ladiaria',
    'robots',
    'search',
    'sorl.thumbnail',
    'shorturls',
    'less',
    'django_user_agents',
    'updown',
    'materialize',
    'crispy_forms',
    'crispy_forms_materialize',
    'actstream',
    'django.contrib.messages',
    'signupwall',
    'homev3',
    'cartelera.config.CarteleraConfig',
    'markdown',
    'django_bleach',
    'django_markdown',
    'django_markup',
    'comunidad',
    'appconf',
    'star_ratings',
    'tagging_autocomplete_tagit',
    'avatar',
    'endless_pagination',
    'notification',
    'django.contrib.flatpages',
    'epubparser',
    'dashboard',
    'django_filters',
    'rest_framework',
    'compressor',
    'favit',
    'social_django',
)

SITE_ID = 1

# photologue app need to add a custom migration
MIGRATION_MODULES = {'photologue': 'photologue_ladiaria.photologue_migrations'}

ADMIN_SHORTCUTS = [
    {
        'title': u'Edición',
        'shortcuts': [
            {
                'url_name': 'admin:core_edition_changelist',
                'title': 'Ediciones',
            },
            {
                'url_name': 'admin:core_edition_add',
                'title': u'Crear edición',
            },
            {
                'url_name': 'admin:core_article_add',
                'title': u'Crear Artículo',
            },
        ],
    },
    {
        'title': 'Reportes',
        'shortcuts': [
            {
                'url': '/dashboard/',
                'title': u'Estadísticas de usuarios',
            },
        ],
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 20,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
}

ACTSTREAM_SETTINGS = {'FETCH_RELATIONS': False, 'USE_PREFETCH': True}

CRISPY_ALLOWED_TEMPLATE_PACKS = ('bootstrap', 'uni_form', 'bootstrap3', 'bootstrap4', 'materialize_css_forms')
CRISPY_TEMPLATE_PACK = 'materialize_css_forms'

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django_cookies_samesite.middleware.CookiesSameSite',
    'core.middleware.AMP.FlavoursCookieSecure',
    'django_mobile.cache.middleware.UpdateCacheFlavourMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',              # runs during the response phase (top -> last)
    'core.middleware.cache.AnonymousResponse',                    # hacks cookie header for anon users (resp phase)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'subdomains.middleware.SubdomainMiddleware',
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    'libs.middleware.url.UrlMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'core.middleware.threadlocals.ThreadLocals',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'signupwall.middleware.SignupwallMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'core.middleware.cache.AnonymousRequest',                     # hacks cookie header for anon users (req phase)
    'django_mobile.cache.middleware.FetchFromCacheFlavourMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',           # runs during the request phase (top -> first)
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'core.middleware.AMP.OnlyArticleDetail',
)

LANGUAGES = (
    ('es', 'Español'),
)
USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'es'
LOCAL_LANG = 'es'
DEFAULT_CHARSET = 'utf-8'
LOCAL_COUNTRY = 'UY'

DATE_INPUT_FORMATS = (
    '%Y-%m-%d', '%d/%m/%Y', '%d/%m/%y',  # 2006-10-25, 25/10/2006, 25/10/06
)
DATETIME_FORMAT = 'j N, Y, P'

DATETIME_INPUT_FORMATS = (
    '%d/%m/%Y %H:%M',     # '10/25/2006 14:30:59'
)

ROOT_URLCONF = 'urls'

DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000

# Base
BASE_SUB = None
DEFAULT_PUB = 'default'

FIRST_DAY_OF_WEEK = 0     # 0 is Sunday
# Convert to calendar module, where 0 is Monday :/
FIRST_DAY_OF_WEEK_CAL = (FIRST_DAY_OF_WEEK - 1) % 7

HOME_PUBLICATIONS = []

HASHIDS_SALT = 'top_secret_salt_phrase'

# A dictionary of urlconf module paths, keyed by their subdomain.
SUBDOMAIN_URLCONFS = {
    None: 'urls',  # no subdomain, e.g. ``example.com``
}

# MEDIA
MEDIA_ROOT = PROJECT_ABSOLUTE_DIR + '/media/'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

CSS_URL = '%scss/' % MEDIA_URL
IMG_URL = '%simg/' % MEDIA_URL
JS_URL = '%sjs/' % MEDIA_URL
SWF_URL = '%sswf/' % MEDIA_URL

mimetypes.add_type("image/svg+xml", ".svg", True)
mimetypes.add_type("image/svg+xml", ".svgz", True)

# AVATAR
AVATAR_DEFAULT_IMAGE = 'identicon'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['127.0.0.1:11211']
    }
}

# required for django mobile.
# TODO: search for a django-mobile replacement because last version is not compatible with new "TEMPLATE" setting.
TEMPLATE_LOADERS = (
    (
        'django_mobile.loader.CachedLoader',
        (
            'django_mobile.loader.Loader',
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
    ),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(PROJECT_ABSOLUTE_DIR, 'templates'), join(PROJECT_ABSOLUTE_DIR, 'apps')],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'context_processors.urls',
                'context_processors.site',
                'context_processors.publications',
                'context_processors.gtm',
                'context_processors.main_menus',
                'django.template.context_processors.static',
                'apps.core.context_processors.aniosdias',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
                'django.template.context_processors.tz',
                'adzone.context_processors.get_source_ip',
                'django_mobile.context_processors.flavour',
                'apps.thedaily.context_processors.permissions',
                'django.template.context_processors.csrf',
            ],
            'loaders': TEMPLATE_LOADERS,
        },
    }
]

FIXTURE_DIRS = (join(PROJECT_ABSOLUTE_DIR, 'fixtures'), )

# EMAIL
EMAIL_FAIL_SILENTLY = False

NOTIFICATIONS_FROM_NAME = 'utopia cms'
NOTIFICATIONS_FROM_ADDR1 = 'suscriptores@example.com'
NOTIFICATIONS_FROM_ADDR2 = 'ventas@example.com'
NOTIFICATIONS_TO_ADDR = 'suscripciones@example.com'
NOTIFICATIONS_FROM_MX = NOTIFICATIONS_FROM_ADDR1

NEWSLETTER_IMG_FORMAT = 'jpg'

SENDNEWSLETTER_LOGFILE = '/var/log/utopiacms/sendnewsletter/%s-%s.log'

# apps

# background tasks
MAX_ATTEMPTS = 1

# core
# publications that use the root url as their home page
CORE_PUBLICATIONS_USE_ROOT_URL = [DEFAULT_PUB]

# slugs of the categories to update their modules after some modifications
CORE_UPDATE_CATEGORY_HOMES = []

# log user visits, disbale on critical performance issues
CORE_LOG_ARTICLE_VIEWS = True

# enable related articles in article detail
CORE_ENABLE_RELATED_ARTICLES = True

# mongodb databases for user and anon article visits
CORE_MONGODB_ARTICLEVIEWEDBY = 'ldsocial_core_articleviewedby'
CORE_MONGODB_ARTICLEVISITS = 'ldsocial_core_articlevisits'
SIGNUPWALL_MONGODB_VISITOR = 'ldsocial_signupwall_visitor'

# Change to false if the signupwall middleware is removed
SIGNUPWALL_ENABLED = True

# thedaily
SUBSCRIPTION_EMAIL_SUBJECT = u'Nueva suscripción'
PROMO_EMAIL_SUBJECT = u'Nueva promoción'
SUBSCRIPTION_EMAIL_TO = [NOTIFICATIONS_TO_ADDR]
SUBSCRIPTION_BY_PHONE_EMAIL_TO = SUBSCRIPTION_EMAIL_TO
MAX_USERS_API_SESSIONS = 3
THEDAILY_SUBSCRIPTION_TYPE_CHOICES = (
    ('DDIGM', u'Suscripción Ilimitada'),
    ('PAPYDIM', u'Suscripción papel'),
)
THEDAILY_PROVINCE_CHOICES = []
THEDAILY_WELCOME_TEMPLATE = 'welcome.html'
THEDAILY_DEFAULT_CATEGORY_NEWSLETTERS = []  # category slugs for add default category newsletters in new accounts

# photologue
DEFAULT_BYLINE = 'Difusión, S/D de autor.'

# django-tagging and autocomplete-taggit
FORCE_LOWERCASE_TAGS = False
TAGGING_AUTOCOMPLETE_JS_BASE_URL = '%sjs/jquery-tag-it-utopia/' % STATIC_URL
TAGGING_AUTOCOMPLETE_JQUERY_UI_FILE = 'jquery-ui.min.js'

# home
PUBLISHING_TIME = '05:00'  # 'HH:MM'

# default logos
HOMEV3_LOGO = HOMEV3_LOGO_FOOTER = 'img/logo-utopia.png'
HOMEV3_SECONDARY_LOGO = 'img/logo-utopia-secondary.png'
HOMEV3_LOGO_PRINTABLE = 'img/logo-utopia-printable.png'
HOMEV3_LOGO_ALT_TEXT = 'utopia logo'

# default footer template
HOMEV3_FOOTER_TEMPLATE = 'footer.html'

# django reCaptcha
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True

# exchange
EXCHANGE_UPDATE_MODULE = 'exchange.brou'

# adzone
ADZONE_LOG_AD_IMPRESSIONS = True
ADZONE_LOG_AD_CLICKS = True

SHORTEN_MODELS = {
    'A': 'core.article',
    'U': 'short.url',
}

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
}

AUTH_USER_EMAIL_UNIQUE = True
AUTH_PROFILE_MODULE = 'thedaily.Subscriber'

# login_required decorator redirects here
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL = '/usuarios/error/login/'

MESSAGETAGS = {messages.ERROR: 'danger', }

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Opciones de django-social-auth
SOCIAL_ADMIN_EMAIL_TO = ['social-admin@ladiaria.com.uy']
SOCIAL_AUTH_GOOGLE_OAUTH2_STRATEGY = 'social_django.strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social_django.models.DjangoStorage'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/plus.me',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile']
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'libs.social_auth_pipeline.get_phone_number',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
SOCIAL_AUTH_URL_NAMESPACE = 'social'

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

BLEACH_STRIP_TAGS = True

# Online sync User fields with CRM (empty, using hardcoded fields only)
CRM_UPDATE_SUBSCRIBER_FIELDS = {}
# Online sync User fields with CRM enabled by default
CRM_UPDATE_USER_ENABLED = True

# PWA
PWA_SERVICE_WORKER_TEMPLATE = 'core/templates/sw/serviceworker.js'
PWA_SERVICE_WORKER_VERSION = 1

try:
    UTILS_MODULE = __import__('utils', fromlist=[PROJECT_ABSOLUTE_DIR])
except ImportError as e:
    print(e)

FREEZE_TIME = None

# Override previous settings with values in local_settings.py settings file.
from local_settings import *

SITE_URL = '%s://%s/' % (URL_SCHEME, SITE_DOMAIN)
ROBOTS_SITEMAP_URLS = [SITE_URL + 'sitemap.xml']
LOCALE_NAME = LOCAL_LANG + '_' + LOCAL_COUNTRY + '.UTF8'

if FREEZE_TIME:
    freezer = freeze_time(FREEZE_TIME)
    freezer.start()

ABSOLUTE_URL_OVERRIDES = {'auth.user': SITE_URL + "usuarios/perfil/editar/"}
