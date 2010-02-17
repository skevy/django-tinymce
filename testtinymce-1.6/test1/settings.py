from os.path import dirname, join

PROJECT_ROOT = dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = join(PROJECT_ROOT, 'dev.db')

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = join(PROJECT_ROOT, "media")
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/static/admin/'

SECRET_KEY = '@df*#7zi(7c6w+mgwd!ihus-#z8ljz%ni54sv=t@arz9mps(^j'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'test1.urls'

TEMPLATE_DIRS = ()

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'tinymce',
)

try:
    import staticfiles
    INSTALLED_APPS += ('staticfiles',)
    STATIC_URL = '/media/static/'
    STATIC_ROOT = join(PROJECT_ROOT, 'static')
except:
    print "staticfiles not installed"
