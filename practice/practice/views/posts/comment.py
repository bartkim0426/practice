from django.shortcuts import redirect
from practice.models import Post


def comment_create(request, post_id):
    content = request.POST.get("content")

    post = Post.objects.get(id=post_id)
    comment = post.comment_set.create(
            content = content
            )

    return redirect(comment)
