"""
Django settings for mobileStore project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9bo3_6@$s=^gvb$%bnaf&)zbns(6d#a_$g5bz8aa)a4#t4y&@r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'http://127.0.0.1:8000/',#! in avali dar model ha astefadeh shodeh
    'localhost',
    '127.0.0.1',
    # "chrome-extension://eejfoncpjfgmeleakejdcanedmefagga",
]


CSRF_TRUSTED_ORIGINS = ['chrome-extension://eejfoncpjfgmeleakejdcanedmefagga']

# CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
# SESSION_COOKIE_DOMAIN = [
#     '127.0.0.1',
#     "http://localhost:8080",
#     'http://127.0.0.1:8000/',
#     'localhost',
#     ]
# Public_Host = "ALLOWED_HOSTS[0]"


# Application definition



AUTH_USER_MODEL = 'account.User'



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    "corsheaders",
    # 'dj_rest_auth',
    'djoser',
    
    #? related dj_rest_auth
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'dj_rest_auth.registration',

    # 'allauth.socialaccount.providers.google',
    # 'mobileStore_Social',
    #?

    # "social_django",

    "rest_framework_simplejwt.token_blacklist",


    'mobileStore_product',
    'mobileStore_product_category',
    'mobileStoreSlider',
    'mobileStore_settings',
    'mobileStore_news',
    'mobileStore_Founders',
    'account',
    # 'mobileStore_account',
    # 'mobileStore_Social',
]


SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    "corsheaders.middleware.CorsMiddleware",

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "social_django.middleware.SocialAuthExceptionMiddleware",

    #?
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'mobileStore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = 'mobileStore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'mobileStoreDatabase',
#         # 'CLIENT': {
#         #    'host': 'your-db-host',
#         # }
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True


LANGUAGE_CODE = 'fa-ir'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tehran'
#locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")
USE_I18N = True

USE_L10N = True

USE_TZ = True

# AUTH_USER_MODEL = 'mobileStore_Social.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


# ACCOUNT_EMAIL_VERIFICATION = "none"

# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_CREDENTIALS = True

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = env("EMAIL_PORT", default=587)
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_USE_TLS = True

# SOCIALACCOUNT_PROVIDERS = {
#     "google": {
#         "APP": {
#             "client_id": "751970675392-t4kssidau1tu5jnhh9msjk9cj1hejtcv.apps.googleusercontent.com",  # replace me
#             "secret": "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",        # replace me
#             "key": "",                               # leave empty
#         },
#         "SCOPE": [
#             "profile",
#             "email",
#         ],
#         "AUTH_PARAMS": {
#             "access_type": "online",
#         },
#         "VERIFIED_EMAIL": True,
#     },
# }

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config("GOOGLE_CLIENT_ID")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config("GOOGLE_SECRET")



# Google OAuth2 settings
# BASE_FRONTEND_URL = os.environ.get('DJANGO_BASE_FRONTEND_URL', default='http://localhost:3000')
# BASE_FRONTEND_URL = 'http://localhost:8080'#! tavajoh shavad dar server bayad avaz shavad
# GOOGLE_OAUTH2_CLIENT_ID = config('GOOGLE_OAUTH2_CLIENT_ID')
# GOOGLE_OAUTH2_CLIENT_SECRET = config('GOOGLE_OAUTH2_CLIENT_SECRET')


SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ["first_name", "last_name"]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}


DJOSER = {
    # "SERIALIZERS": {
    #     "user_create": "account.serializers.UserCreateSerializer",  # custom serializer
    # },

    # 'USER_CREATE_PASSWORD_RETYPE': True,
    # 'SEND_CONFIRMATION_EMAIL': True,
    # 'SEND_ACTIVATION_EMAIL': True,
    # 'ACTIVATION_URL': 'activate/{uid}/{token}',
    # 'HIDE_USERS': True,
    # 'SERIALIZERS': {
    #     'user': 'account.serializers.UserCreateSerializer',
    #     'user_create': 'account.serializers.UserCreateSerializer',
    #     'current_user': 'account.serializers.UserSerializer',
    # },
    # 'EMAIL': {
    #     'activation': 'account.email.ActivationEmail',
    #     'confirmation': 'account.email.ConfirmationEmail',
    # },

    # 'CREATE_SESSION_ON_LOGIN': True,

    'TOKEN_MODEL': 'rest_framework.authtoken.models.Token',

    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    # "SOCIAL_AUTH_TOKEN_STRATEGY": "account.token.TokenStrategy",
    # "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": ["http://localhost:3000"],
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": ["http://localhost:8080"],#!
    "SERIALIZERS": {
        "user_create": "account.serializers.UserCreateSerializer",
        "user": "account.serializers.UserCreateSerializer",
        "current_user": "account.serializers.UserCreateSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
    'EMAIL': {
        'activation': 'account.email.ActivationEmail',
        'confirmation': 'account.email.ConfirmationEmail',
        'password_reset': 'account.email.PasswordResetEmail',
        'password_changed_confirmation': 'account.email.PasswordChangedConfirmationEmail',
    },
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static_cdn", "media_root")

STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn' , "static_root")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets")
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# CORS_ALLOWED_ORIGINS = [
#     "https://example.com",
#     "https://sub.example.com",
#     "http://localhost:8080",
#     "http://127.0.0.1:9000",
# ]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    ]

CORS_ORIGIN_ALLOW_ALL = True
 
 
