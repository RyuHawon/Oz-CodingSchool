from django.db import models
from posts.models import Post
from users.models import CustomUser


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
