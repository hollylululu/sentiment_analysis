import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g@b=tbk%*wa0gohdzv^5p7s4@e5!0nwi2oij=gk=x!ej(!$hs%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sentimentAnalysis',
    'crispy_forms',
    'django_celery_results',
    'reset_migrations',
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

ROOT_URLCONF = 'sentiment_analysis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": ["sentimentAnalysis/templates/"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        'libraries':{
            'index': 'sentimentAnalysis.templatetags.index',

            }
        },
    },
]

WSGI_APPLICATION = 'sentiment_analysis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # We use postgresql for Database engine
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sentimentdb',
        'USER': 'jooheekwon',
        'PASSWORD': 'victoriaDB',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


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

LOGGING = { 'version': 1, 'disable_existing_loggers': False, 'handlers': { 'file': { 'level': 'DEBUG', 'class': 'logging.FileHandler', 'filename': 'debug.log', }, }, 'loggers': { 'django': { 'handlers': ['file'], 'level': 'DEBUG', 'propagate': True, }, }, }


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#for google Authentication
AUTHENTICATION_BACKENDS = (
 'social.backends.facebook.FacebookOAuth2',
 'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
 'social_core.backends.google.GoogleOpenId',  # for Google authentication
 'social_core.backends.google.GoogleOAuth2',  # for Google authentication
 'django.contrib.auth.backends.ModelBackend',
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    '/var/www/static/',
]

STATIC_ROOT = os.path.join(BASE_DIR,'sentimentAnalysis', 'static')

MEDIA_URL = '/text/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'text')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG
