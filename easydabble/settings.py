import os 
# from .secret import SECRET_KEY
#/

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# for gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'EMAIL_HOST_USER'
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hann'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


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
	'storages',
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



DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

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

# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_root")

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

access_key = 'AKIAJAQZME4IJ2ZUTMEQ'
secret_key = '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'

AWS_ACCESS_KEY_ID = access_key
AWS_SECRET_ACCESS_KEY = secret_key
AWS_STORAGE_BUCKET_NAME = 'easydabble'

STATICFILES_STORAGE = 'easydabble.s3utils.StaticRootS3BotoStorage'
# DEFAULT_FILE_STORAGE = 'easydabble.s3utils.MediaRootS3BotoStorage'

S3_URL = 'http://%s.s3.amazonaws.com/' %AWS_STORAGE_BUCKET_NAME
MEDIA_URL = S3_URL + "media/"
STATIC_URL = S3_URL + "static/"
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

DEBUG_TOOLBAR_PANELS = [
 'debug_toolbar.panels.versions.VersionsPanel',
 'debug_toolbar.panels.timer.TimerPanel',
 'debug_toolbar.panels.settings.SettingsPanel',
 'debug_toolbar.panels.headers.HeadersPanel',
 'debug_toolbar.panels.request.RequestPanel',
 'debug_toolbar.panels.sql.SQLPanel',
 # 'debug_toolbar.panels.staticfiles.StaticFilesPanel',                                                                                                                                    
 'debug_toolbar.panels.templates.TemplatesPanel',
 'debug_toolbar.panels.cache.CachePanel',
 'debug_toolbar.panels.signals.SignalsPanel',
 'debug_toolbar.panels.logging.LoggingPanel',
 'debug_toolbar.panels.redirects.RedirectsPanel',
]