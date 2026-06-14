# notices/admin.py
from django.contrib import admin
from .models import Category, Notice

admin.site.register(Category)
admin.site.register(Notice)
