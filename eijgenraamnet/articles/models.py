#!/usr/bin/env python3
from django.db import models as m
from django.urls import reverse


# Create your models here.
class Author(m.Model):
    first_name = m.CharField(max_length=128)
    last_name = m.CharField(max_length=128)
    dob = m.DateField()

    def __str__(self):
        return f"{self.first_name}, {self.dob}"


class Post(m.Model):
    title = m.CharField(max_length=64)
    slug = m.SlugField(default="", blank=True, null=False, db_index=True)
    header_image = m.ImageField(upload_to="static/images/", null=True)
    date = m.DateField()
    author = m.ForeignKey(Author, on_delete=m.SET_NULL, null=True)
    excerpt = m.TextField(max_length=200)
    content = m.TextField(max_length=20000)

    def __str__(self):
        return f"{self.title}, ({self.date})"

    def get_absolute_url(self):
        return reverse("post-page", args=[self.slug])


class Comment(m.Model):
    post = m.ForeignKey(Post, on_delete=m.CASCADE, null=False, related_name="comments")
    username = m.CharField(max_length=64)
    date = m.DateField()
    text = m.TextField(max_length=1000)

    def __str__(self):
        return f"{self.username}, {self.date}"
