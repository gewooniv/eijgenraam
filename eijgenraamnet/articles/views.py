#!/usr/bin/env python3
# # Create your views here.

import datetime as dt

from dateutil import tz
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import CommentForm
from .models import Comment
from .models import Post


def get_posts():
    return Post.objects.all().order_by("date")


def get_comments_per_post(post):
    return Comment.objects.filter(post=post).order_by("date")


# Create your views here.
class MainPageView(ListView):
    template_name = "../templates/pages/articles/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "featured_posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(featured=True)


class PostsView(ListView):
    template_name = "../templates/pages/articles/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


class PostView(View):
    def get(self, request, slug):
        single_post = get_object_or_404(Post, slug=slug)

        context = {
            "post": single_post,
            "comment_form": CommentForm(),
            "all_comments": get_comments_per_post(single_post),
        }

        return render(request, "../templates/pages/articles/post-page.html", context)

    def post(self, request, slug):
        single_post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = single_post
            comment.date = dt.datetime.now(tz=tz.gettz("Europe/Amsterdam")).date()
            comment.save()

            return HttpResponseRedirect(reverse("post-page", args=[slug]))

        context = {
            "post": single_post,
            "comment_form": form,
            "all_comments": get_comments_per_post(single_post),
        }

        return render(request, "articles/post-page.html", context)
