from django.contrib import admin

# import your models from apps

from .models import Url

# Register your models here.
admin.site.register(Url)