"""
WSGI config for testproject project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
from __future__ import unicode_literals

import os
import sys

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application

PROJECT_PATH = os.path.abspath(os.path.split(__file__)[0])
PROJECT_PARENT = os.path.abspath(os.path.split(PROJECT_PATH)[0])
sys.path.append(PROJECT_PATH)
sys.path.append(PROJECT_PARENT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")

application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
