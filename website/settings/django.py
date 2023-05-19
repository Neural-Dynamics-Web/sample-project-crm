# region				-----External Imports-----
from pathlib import Path
import sys
import os
# endregion

# region			  -----Supporting Variables-----
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# endregion

# region		     -----Application Definition-----
THIRD_PARTY_APPS = [
    'jazzmin',
    'django_ckeditor_5',
    'phonenumber_field',
    'admin_auto_filters',
    'mdeditor',
]

INSTALLED_APPS = [
    'staff',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites'
]

USER_APPS = [
    'development',
    'department',
    'finance',
    'sales',
    'geo'
]

LANGUAGE_CODE = "en"

LANGUAGES = (
  ('en', 'English'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

INSTALLED_APPS = THIRD_PARTY_APPS\
               + INSTALLED_APPS\
               + USER_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.static',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'

LOGIN_URL = '/admin/login/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1
# endregion

# region			  -----Password Validations-----
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
# endregion

# region			  -----Internationalization-----
TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATETIME_INPUT_FORMATS = ('%d/%m/%Y %H:%M', '%Y-%m-%d %H:%M')
DATE_INPUT_FORMATS = ('%d/%m/%Y', '%Y-%m-%d')

DATETIME_FORMAT = "d/m/Y G:i"
DATE_FORMAT = "d/m/Y"
# endregion

# region				  -----Static files-----
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_ROOT = os.path.join(BASE_DIR, 'allstaticfiles')

STATICFILE_DIR = os.path.join(BASE_DIR, 'allstaticfiles/static')
STATICFILES_DIRS = (
    STATICFILE_DIR,
    os.path.join(BASE_DIR, 'website/static')
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)
# endregion

# region				     -----Fields-----
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'staff.Staff'
# endregion

# region				     -----Medias-----
MEDIA_FOLDER = 'media'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_FOLDER)
MEDIA_URL = '/media/'
# endregion

# region			   -----Working Processes-----
PROJECT_MANAGEMENT_MULTIPLIER = 0.25
PROJECT_MANAGEMENT_RATE = 20
TESTING_MULTIPLIER = 0.3
WORKING_DAY_DURATION = 8
TESTING_RATE = 15
# endregion

X_FRAME_OPTIONS = "SAMEORIGIN"

# region				    -----Loggings-----
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            '()': 'djangocolors_formatter.DjangoColorsFormatter',
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            '()': 'djangocolors_formatter.DjangoColorsFormatter',
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        "errors_log": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "errors.log"),
            "maxBytes": 1024 * 1024 * 10,
            "backupCount": 7,
            "formatter": "verbose"
        },
    },
    # 'loggers': {
    #     '': {
    #         'level': 'DEBUG',
    #         'handlers': ['console'],
    #     },
    #     'django.request': {
    #         'handlers': ['mail_admins', 'errors_log', 'console'],
    #         'level': 'DEBUG',
    #         'propagate': False,
    #     },
    #     'django.db.backends': {
    #         'level': 'DEBUG',
    #         'handlers': ['console'],
    #     }
    # }
}
# endregion


JIRA_TOKEN = os.environ.get("JIRA_TOKEN")

JIRA_USERNAME = os.environ.get("JIRA_USERNAME")
JIRA_OWNER_ID = os.environ.get("JIRA_OWNER_ID")
