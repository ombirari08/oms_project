import os
from pathlib import Path
import environ # Ensure `django-environ` is installed

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
env = environ.Env()
env_path = os.path.join(BASE_DIR, ".env")  # Make sure this points to your correct .env file path
if os.path.exists(env_path):
    environ.Env.read_env(env_path)
else:
    raise FileNotFoundError(f".env file not found at {env_path}")

# Load secret key from .env
SECRET_KEY = env("DJANGO_SECRET_KEY", default="your-default-secret-key")

# Debug mode (ensure it's False in production)
DEBUG = env.bool("DJANGO_DEBUG", default=False)

# Allowed hosts (Ensure these values exist in your .env file)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])


# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'social_django',
    'orders',
]

# Authentication settings
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


# Google OAuth Credentials from .env
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env("GOOGLE_CLIENT_ID")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env("GOOGLE_CLIENT_SECRET")


SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
SOCIAL_AUTH_URL_NAMESPACE = "social"
#LOGIN_REDIRECT_URL = "/dashboard/"
#LOGOUT_REDIRECT_URL = "/"
#SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'http://127.0.0.1:8000/complete/google/'


# # Define context_processors after TEMPLATES is set
# TEMPLATES[0]["OPTIONS"]["context_processors"] += [
#     "django.template.context_processors.csrf",
# ]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oms_project.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "orders" / "templates"],  # Ensure this folder exists
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # Add this for Google OAuth
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


WSGI_APPLICATION = 'oms_project.wsgi.application'

# Database Configuration (MySQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oms_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET default_storage_engine=INNODB, sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

