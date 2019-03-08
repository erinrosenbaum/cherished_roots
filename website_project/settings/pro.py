from .base import *

DEBUG = False

ADMINS = (
    ('erinrosenbaum', 'erinrosenbaum@yahoo.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'my_website_db',
        'USER': 'mac',
        'PASSWORD': 'Baums226',
    }
}

X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
