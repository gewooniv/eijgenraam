#!/usr/bin/env python3
from django.shortcuts import render

from .models import Picture


# Create your views here.
def index(request):
    pictures = Picture.objects.all()
    context = {"pictures": pictures}
    return render(request, "../templates/pages/gallery/gallery.html", context)
