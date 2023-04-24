from django.contrib import admin

# Register your models here.
from .models import Userinfo,Book

admin.site.register(Userinfo)
admin.site.register(Book)