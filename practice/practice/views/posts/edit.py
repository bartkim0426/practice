from django.shortcuts import render
from practice.models import Post


def edit(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(
            request,
            "posts/edit.html",
            {"post": post,},
            )
