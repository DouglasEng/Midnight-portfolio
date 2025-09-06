from .settings_base import *

# Segurança
SECRET_KEY = 'your-public-placeholder-key'
DEBUG = True
ALLOWED_HOSTS = ['*']  # ou deixar vazio

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_public.sqlite3',
    }
}
