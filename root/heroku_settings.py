import django_heroku
from root.base_settings import *



ALLOWED_HOSTS = ['johansson-app.herokuapp.com']

DEBUG = True

# Values are set in heroku dashboard
SECRET_KEY = os.environ.get('SECRET_KEY', 'NOT SET')


#  Add configuration for static files storage using whitenoise, heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE += [
    # 'django_user_agents.middleware.UserAgentMiddleware', # User agent
    'whitenoise.middleware.WhiteNoiseMiddleware', # whitenoise, heroku
]

MIDDLEWARE_CLASSES = [
    'whitenoise.middleware.WhiteNoiseMiddleware', # whitenoise, heroku
]

# Activate Django-Heroku.
django_heroku.settings(locals())