"""
WSGI config for djangoproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import getpass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproject.settings")

if getpass.getuser() == "I321761":
    print("! Office environment, set http proxy")
    os.environ['http_proxy'] = "http://proxy.pal.sap.corp:8080"
    os.environ['https_proxy'] = "http://proxy.pal.sap.corp:8080"

application = get_wsgi_application()
