#!/usr/bin/env python3
from django.db import models as m


# Create your models here.
class Category(m.Model):
    name = m.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Picture(m.Model):
    name = m.CharField(max_length=255)
    image = m.ImageField(upload_to="images/")
    description = m.TextField()
    date = m.DateTimeField(auto_now_add=True)
    category = m.ForeignKey(Category, on_delete=m.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}, {self.date}"
