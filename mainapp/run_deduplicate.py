import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainapp.settings")
django.setup()

from myproxy.utils.SortDt import sort

if __name__ == '__main__':
    sort()
