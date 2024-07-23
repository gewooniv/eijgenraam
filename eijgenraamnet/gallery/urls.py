from django.urls import path

from . import views

urlpatterns = [
    path("gallery", views.PostList.as_view(), name="gallery"),
]
