from django.shortcuts import render
from django.core.paginator import Paginator
from practice.models import Post


def list(request):
    page = request.GET.get("page") or 1
    per = request.GET.get("per") or 3

    posts = Post.objects.public()
    p = Paginator(posts, per)

    posts = p.page(page)
    
    return render(
            request,
            "posts/list.html",
            {"posts": posts},
            )
