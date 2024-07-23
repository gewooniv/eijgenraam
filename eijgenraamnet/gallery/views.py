#!/usr/bin/env python3
from django_filters.views import FilterView

from .filtersets import PictureFilter
from .models import Picture


# Create your views here.
class PostList(FilterView):
    template_name = "../templates/pages/gallery/gallery.html"
    model = Picture
    context_object_name = "pictures"
    filterset_class = PictureFilter
