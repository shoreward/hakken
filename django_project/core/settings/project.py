from .contrib import *

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # Or path to database file if using sqlite3.
        'NAME': 'hakken',
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
    }
}

# Project apps
INSTALLED_APPS += (
    'leaflet',
    'djgeojson',
    'web',
    'projects',
    'workunits',
    'admin',
    'workbench'
)

# Set debug to false for production
DEBUG = TEMPLATE_DEBUG = False


PIPELINE_JS = {
    'contrib': {
        'source_filenames': (
            'js/jquery-1.10.2.min.js',
            'js/csrf-ajax.js',
            'js/underscore-min.js',
            'js/semantic.min.js',
        ),
        'output_filename': 'js/contrib.js',
    }
}

PIPELINE_CSS = {
    'contrib': {
        'source_filenames': (
            'css/semantic.min.css',
            'css/custom.css'
        ),
        'output_filename': 'css/contrib.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    }
}

LOGIN_REDIRECT_URL = '/'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (0, 0),
    'DEFAULT_ZOOM': 4,
    'RESET_VIEW': False,
    'PLUGINS': {
        'omnivore': {
            'js': 'js/leaflet-omnivore.min.js',
            'auto-include': True,
        },
        'sync': {
            'js': 'js/leaflet.sync.js',
            'auto-include': True,
        },
        'bing': {
            'js': 'js/leaflet.bing.js',
            'auto-include': True,
        }
    }
}
