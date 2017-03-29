from django.db import models
from django.urls.base import reverse


class Comment(models.Model):
    post = models.ForeignKey("Post")

    content = models.TextField()

    is_public = models.BooleanField(
            default = True
            )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse(
               "posts:detail",
               kwargs = {"post_id": self.post_id},
               ) + "#comment-" + str(self.id)
