from django.shortcuts import redirect, render
from practice.models import Post


def delete(request, post_id):
    post = Post.objects.get(id=post_id)

    post.delete()
    
    return redirect(
            render(
                request,
                "posts/list.html",
                {},
                )
            )
