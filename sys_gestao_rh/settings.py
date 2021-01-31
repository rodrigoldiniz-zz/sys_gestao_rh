from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = '*wriztg_sei-i$9o#9von$yyk_l92b^b!@2%p0=(el@$0&&c@y'

DEBUG = True


ALLOWED_HOSTS = []


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_APPS = [
    'bootstrapform',
]

PROJECT_APPS = [
        'apps.empresas',
        'apps.funcionarios',
        'apps.departamentos',
        'apps.documentos',
        'apps.registro_hora_extra',
        'apps.core',
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

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + PROJECT_APPS

ROOT_URLCONF = 'sys_gestao_rh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'sys_gestao_rh.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DJANGO_CONTRIB_VALID = 'django.contrib.auth.password_validation'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': DJANGO_CONTRIB_VALID + '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': DJANGO_CONTRIB_VALID + '.MinimumLengthValidator',
    },
    {
        'NAME': DJANGO_CONTRIB_VALID + '.CommonPasswordValidator',
    },
    {
        'NAME': DJANGO_CONTRIB_VALID + '.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


STATICFILES_DIRS = [
    BASE_DIR / "static",
]


LOGIN_REDIRECT_URL = 'core:home'

LOGOUT_REDIRECT_URL = 'login'
