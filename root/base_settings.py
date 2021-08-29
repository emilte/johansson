from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

"""
Base settings has all configurations that are used by the project in general.
It is also setup with strict configurations suitable for development.

Production server must:
1. Create its own settings file eg. prod_settings
2. from root.base_settings import *
3. Set SECRET_KEY
4. Set ENV
5. Configure DATABASES
6. Specify settings to use
"""

# Environments:
# useful in eg. templates
# override env in current settings (should not stay in BASE)
BASE = "BASE"
DEV = "DEV"
PROD = "PROD"
ENV = BASE

# Custom User model
# from django.contrib.auth import get_user_model; User = get_user_model()
AUTH_USER_MODEL = "accounts.User"

# LOGIN_URL = ''
# LOGIN_REDIRECT_URL = ''
# LOGOUT_REDIRECT_URL = ''

DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticroot'

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE  = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SESSION_COOKIE_NAME = 'sessionid'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 24*60*60*7
SESSION_EXPIRE_AT_BROWSER_CLOSE = False


INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # main apps
    'root',
    'accounts',
    'library',    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
   # 'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

WSGI_APPLICATION = 'root.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'nb'
TIME_ZONE = 'Europe/Oslo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTHENTICATION_BACKENDS = {
#     'accounts.authentication.EmailOrUsernameModelBackend',
# }

# django_debug_toolbar:
SHOW_COLLAPSED = True

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS += [
    'debug_toolbar',
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]
# End: django_debug_toolbar ----------------------------------------------------

# compressor / django-libsass:
INSTALLED_APPS += [
    'compressor', # django-libsass
    
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'), # django-libsass
)

STATICFILES_FINDERS += [
    'compressor.finders.CompressorFinder', # django-libsass
]
# End: compressor ----------------------------------------------------


try:
    from env import * # star is necessary
    print("Loading env.py environment variables...")
except Exception as e:
    pass
    # print("env.py was not imported")

# Quick fix for avoiding concurrency issues related to db access
# https://docs.djangoproject.com/en/1.10/topics/db/transactions/#django.db.transaction.on_commit
# https://medium.com/@hakibenita/how-to-manage-concurrency-in-django-models-b240fed4ee2
ATOMIC_REQUESTS = True

checklist = {
    # 'DEBUG': DEBUG,
    # 'DATABASES': DATABASES,
}

def check_settings(settings=None):
    print("|\n== CHECK SETTINGS ==")
    for k, v in settings.items():
        print("{} = {}".format(k, v))
    print('|')

# check_settings(checklist)

