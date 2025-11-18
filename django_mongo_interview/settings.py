from pathlib import Path
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

BASE_DIR = Path(__file__).resolve().parent.parent

# --- TODO: Candidate Setup Task 1 ---
# 1. Uncomment the following line to load environment variables from .env
# load_dotenv(BASE_DIR / '.env')
# --- End of TODO ---

SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key-for-local-dev')
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
    'tasks',  # Our new tasks app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', # Disabled for simple API testing
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_mongo_interview.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'django_mongo_interview.wsgi.application'

# We are NOT using Django's default SQL ORM.
DATABASES = {}

# --- TODO: Candidate Setup Task 2 ---
# 1. Uncomment the entire `try...except` block below
#    to initialize the MongoDB connection.
# --- End of TODO ---
# try:
#     MONGO_URI = os.getenv('MONGO_URI')
#     if not MONGO_URI:
#         raise ValueError("MONGO_URI is not set in your .env file")
#     
#     DB_NAME = MONGO_URI.split('/')[-1].split('?')[0]
#     if not DB_NAME:
#         raise ValueError("Could not determine database name from MONGO_URI")
#     
#     mongo_client = MongoClient(MONGO_URI)
#     mongo_client.admin.command('ping') # Test connection
#     
#     MONGO_DB_CLIENT = mongo_client[DB_NAME]
#     print(f"MongoDB connection successful to database: {DB_NAME}")
# 
# except (ConnectionFailure, ValueError) as e:
#     print(f"Error connecting to MongoDB: {e}")
#     MONGO_DB_CLIENT = None
# --- End of TODO ---

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'