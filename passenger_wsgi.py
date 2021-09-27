# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1467716/data/www/ruterm31.com/ruterm')
sys.path.insert(1, '/var/www/u1467716/data/ruterm_env/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ruterm.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()