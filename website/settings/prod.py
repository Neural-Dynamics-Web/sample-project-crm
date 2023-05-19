# region				-----External Imports-----
import glob
import os
# endregion

# region				-----Internal Imports-----
from .django import *
from .project import *
from .third_party import *
# endregion


def docker_swarm_secrets_import() -> None:
    for secret in glob.glob('/run/secrets/*'):
        secret_name=secret.split('/')[-1]
        secret_value=open(secret).read().rstrip('\n')
        os.environ[secret_name] = secret_value

docker_swarm_secrets_import()

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

DATABASES = {
    'default': {
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'USER': os.environ.get('DATABASE_USER'),
        'ENGINE': os.environ.get('ENGINE'),
        'ATOMIC_REQUESTS': True
    }
}

CORS_ALLOWED_ORIGINS = [
    f'http://{os.environ.get("FRONTEND_DOMAIN")}',
    f'https://{os.environ.get("FRONTEND_DOMAIN")}',
    'http://127.0.0.1:3000',
    'http://127.0.0.1',
    'http://localhost:3000',
    'http://localhost'
]

CSRF_TRUSTED_ORIGINS = [
    f'http://{os.environ.get("BACKEND_DOMAIN")}',
    f'https://{os.environ.get("BACKEND_DOMAIN")}',
    'http://127.0.0.1:3000',
    'http://127.0.0.1',
    'http://localhost:3000',
    'http://localhost'
]

