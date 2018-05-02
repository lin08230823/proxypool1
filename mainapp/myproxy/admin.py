from django.contrib import admin
from .models import Proxy,IpAddr
# Register your models here.
admin.site.register(Proxy)
admin.site.register(IpAddr)
