
import os
from .secret import SECRET_KEY, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# for gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

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
	'crispy_forms',
	'embed_video',
	'sitemaps',
	'newsletters',
	'contacts',
	'posts',
	'videos',
	'reviews',
	'users',
	'taggit',
	'debug_toolbar',


	'django.contrib.sites',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
	# 'allauth.socialaccount.providers.facebook',

]

MIDDLEWARE_CLASSES = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'easydabble.urls'

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

WSGI_APPLICATION = 'easydabble.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SESSION_COOKIE_AGE = 31,536,000 

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_root")

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "static"),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_root") 


AUTHENTICATION_BACKENDS = (
	# Needed to login by username in Django admin, regardless of `allauth`
	'django.contrib.auth.backends.ModelBackend',

	# `allauth` specific authentication methods, such as login by e-mail
	'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1


LOGIN_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_USERNAME_REQUIRED = True      # Defaults to True
ACCOUNT_EMAIL_REQUIRED = True 

# SOCIALACCOUNT_PROVIDERS =     {'facebook':

# 	   {'METHOD': 'oauth2',

# 		'SCOPE': ['email'],

# 		'AUTH_PARAMS': {'auth_type': 'reauthenticate'},

# 		'LOCALE_FUNC': lambda request: 'en_US',

# 		'VERSION': 'v2.4'}}

