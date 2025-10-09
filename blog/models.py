# Optional: Order posts by most recent by default
from django.db import models
from django.conf import settings  # ✅ Use settings to link to CustomUser

class Post(models.Model):
    """
    Represents a single blog post.
    - title: The title of the blog post.
    - content: The main body content of the post.
    - published_date: The date and time the post was first published (auto_now_add=True).
    - author: Linked to the custom user model defined in settings.AUTH_USER_MODEL.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
