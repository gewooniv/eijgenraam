#!/usr/bin/env python3
# Register your models here.
from django.contrib import admin

from .models import Author
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ()
    prepopulated_fields = {"slug": ("title",)}
    # list_display
    list_filter = ("author",)


admin.site.register(Author)
