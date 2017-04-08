from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from practice.models import Post


def comment_create(request, post_id):

    content = request.POST.get("content")

    if (request.user.is_authenticated):
        user = request.user

        post = Post.objects.get(id=post_id)
        comment = post.comment_set.create(
                content = content,
                user = user,
                )

        return redirect(comment)

    return redirect("auth:login")

def comment_edit(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.all()
    comment = post.comment_set.get(id=comment_id)

    return render(
            request,
            "posts/comment_edit.html",
            {
            "post": post,
            "comment": comment,
            "comments": comments,
            },
            )

def comment_update(request, post_id, comment_id):
    content = request.POST.get("content")

    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    comment.content = content
    comment.save()

    return redirect(
           comment
           )

def comment_delete(request, post_id, comment_id):
    post = Post.objects.get(id=post_id)
    comment = post.comment_set.get(id=comment_id)

    comment.delete()

    return redirect(
           post
           )
