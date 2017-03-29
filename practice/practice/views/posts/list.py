from django.shortcuts import render
from practice.models import Post


def list(request):
    posts = Post.objects.all()

    return render(
            request,
            "posts/list.html",
            {"posts": posts},
            )
