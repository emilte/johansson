from root.base_settings import *
import django_heroku
import os


ALLOWED_HOSTS = ['johansson-app.herokuapp.com']
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ALLOWED_HOSTS)

# Values are set in heroku dashboard
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ.get('DEBUG', False)


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