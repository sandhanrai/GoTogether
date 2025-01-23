import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # Define BASE_DIR

# GoTogether/settings.py

# Security settings
DEBUG = True  # Enable debugging mode

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Allow requests from localhost

# Secret key for the application
SECRET_KEY = 'django-insecure-!@#your_generated_secret_key_here'  # Replace with a generated key

# Database configuration for MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'GOTOGETHER',  # Set the correct database name
        'USER': 'root',
        'PASSWORD': 'Mysql@1234',
        'HOST': 'localhost',
        'PORT': '3306',  # Default MySQL port
    }
}

# Root URL configuration
ROOT_URLCONF = 'GoTogether.urls'  # Ensure this points to your main urls.py

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rides',
    'booking',
    'payments',
    'feedback',
    'users',
    'schedules',
    'shuttles',
]

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

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add this line
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

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
