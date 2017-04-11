"""
WSGI config for ReptileDB project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

import django.core.handlers.wsgi

if path not in sys.path:
    sys.path.append(path)

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ReptileDB.settings")

