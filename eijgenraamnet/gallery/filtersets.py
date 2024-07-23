import django_filters

from .models import Picture


class PictureFilter(django_filters.FilterSet):
    class Meta:
        model = Picture
        fields = ["category"]
