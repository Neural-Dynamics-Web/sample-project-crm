# region				-----External Imports-----
import os
from dotenv import load_dotenv
# endregion

# region				-----Internal Imports-----
from .django import *
from .project import *
from .third_party import *
# endregion

load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1,0.0.0.0').split(',')

DATABASES = {
    'default': {
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'USER': os.environ.get('DATABASE_USER'),
        'ENGINE': os.environ.get('ENGINE'),
        'ATOMIC_REQUESTS': True,
        'TEST': {
            'NAME': 'tests',
        },
    }
}
