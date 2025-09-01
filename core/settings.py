from pathlib import Path import environ import dj_database_url

BASE_DIR = Path(file).resolve().parent.parent_

Environment
env = environ.Env(DJANGO_DEBUG=(bool, False)) environ.Env.read_env(BASE_DIR / ".env") # local only; Render uses real env vars_

SECRET_KEY = env("DJANGO_SECRET_KEY", default="unsafe-secret-key-change-me") DEBUG = env("DJANGO_DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"]) CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

Apps
INSTALLED_APPS = [ "django.contrib.admin", "django.contrib.auth", "django.contrib.contenttypes", "django.contrib.sessions", "django.contrib.messages", "django.contrib.staticfiles", "rest_framework", "corsheaders", "drf_spectacular", "apps.users", "apps.common", ]_

Middleware
MIDDLEWARE = [ "corsheaders.middleware.CorsMiddleware", "django.middleware.security.SecurityMiddleware", "django.contrib.sessions.middleware.SessionMiddleware", "django.middleware.common.CommonMiddleware", "django.middleware.csrf.CsrfViewMiddleware", "django.contrib.auth.middleware.AuthenticationMiddleware", "django.contrib.messages.middleware.MessageMiddleware", "django.middleware.clickjacking.XFrameOptionsMiddleware", ]

ROOT_URLCONF = "core.urls"_

TEMPLATES = [ { "BACKEND": "django.template.backends.django.DjangoTemplates", "DIRS": [], "APP_DIRS": True, "OPTIONS": { "context_processors": [ "django.template.context_processors.debug", "django.template.context_processors.request", "django.contrib.auth.context_processors.auth", "django.contrib.messages.context_processors.messages", ], }, } ]

WSGI_APPLICATION = "core.wsgi.application"_

Database: SQLite fallback, Postgres when DATABASE_URL is set_
DATABASES = { "default": { "ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3", } }_

DB_URL = env("DATABASE_URL", default="").strip() if DB_URL: DATABASES["default"] = dj_database_url.parse(DB_URL, conn_max_age=600, ssl_require=True)_

Custom user model (apps.users has label 'apps_users' in its AppConfig)_
AUTH_USER_MODEL = "apps_users.User"_

DRF & JWT
REST_FRAMEWORK = { "DEFAULT_AUTHENTICATION_CLASSES": ( "rest_framework_simplejwt.authentication.JWTAuthentication", ), "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema", }

SPECTACULAR_SETTINGS = { "TITLE": "FIT.ME API", "DESCRIPTION": "API docs for FIT.ME MVP", "VERSION": "0.1.0", }_

CORS
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[]) CORS_ALLOW_CREDENTIALS = True

I18N
LANGUAGE_CODE = "en-us" TIME_ZONE = "UTC" USE_I18N = True USE_TZ = True

Static files
STATIC_URL = "static/" STATIC_ROOT = BASE_DIR / "staticfiles"_

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

Security behind proxy (Render)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https") SESSION_COOKIE_SECURE = not DEBUG CSRF_COOKIE_SECURE = not DEBUG

What to do next (super short):

Ensure requirements.txt does NOT include “python-3.11.9”.
Create runtime.txt at repo root with: python-3.11.9
Commit this settings.py and push.
In Render > Settings > Environment, set:
DJANGO_SECRET_KEY = a-long-random-string
DJANGO_DEBUG = false
ALLOWED_HOSTS = .onrender.com,localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS = https://fitme-backend-9hw8.onrender.com
CORS_ALLOWED_ORIGINS = http://localhost:3000
DATABASE_URL = postgresql://USER:NEW_PASSWORD@ep-...neon.tech:5432/neondb?sslmode=require
