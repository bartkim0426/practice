from django.db import models
from django.urls.base import reverse
from django.contrib.auth.models import User


class Comment(models.Model):
    post = models.ForeignKey("Post")
    user = models.ForeignKey(User)

    content = models.TextField()

    is_public = models.BooleanField(
            default = True
            )

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse(
               "posts:detail",
               kwargs = {"post_id": self.post_id},
               ) + "#comment-" + str(self.id)
