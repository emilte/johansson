from root.base_settings import * # star is essensial to set variables

ENV = DEV # Can be used in custom templatetags
print(f"Environment: {ENV}")

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

DEBUG = True

SECRET_KEY = "NOT SET"

# Security
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE  = False
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False
X_FRAME_OPTIONS = 'SAMEORIGIN'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
