
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainapp.settings")
django.setup()

from myproxy.spiders import xici
xici = xici.fetch_xici

if __name__ == '__main__':
    xici()