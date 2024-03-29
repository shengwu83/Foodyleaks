"""
WSGI config for Foodyleaks project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

import sys

path = '/home/sheng/djangoRepo/Foodyleaks'

if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Foodyleaks.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
