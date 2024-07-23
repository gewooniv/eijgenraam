#!/usr/bin/env python3
from django.contrib import admin

from .models import Category
from .models import Picture

# Register your models here.
admin.site.register(Picture)
admin.site.register(Category)
