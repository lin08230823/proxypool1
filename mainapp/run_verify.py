# coding=utf-8
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mainapp.settings")
django.setup()


from myproxy.utils.VerifyProxy import verify


if __name__ == '__main__':
    verify()