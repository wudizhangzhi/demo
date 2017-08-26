# encoding: utf-8
import sys
import os
# from django.core.wsgi import get_wsgi_application

django_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.extend([django_path, ])
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demon.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = "demon.settings"
# application = get_wsgi_application()
import django
django.setup()
