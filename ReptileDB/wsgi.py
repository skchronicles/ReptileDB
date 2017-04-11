"""
WSGI config for ReptileDB project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

import django.core.handlers.wsgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ReptileDB.settings")

application = django.core.handlers.wsgi.WSGIHandler()
