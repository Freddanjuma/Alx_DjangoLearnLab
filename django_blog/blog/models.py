from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model

class Post(models.Model):
    """
    Represents a single blog post.
    - title: The title of the blog post.
    - content: The main body content of the post.
    - published_date: The date and time the post was first published.
                      Automatically set when the post is created (auto_now_add=True).
    - author: A foreign key to Django's built-in User model, indicating who wrote the post.
              A single User can author multiple Posts (one-to-many relationship).
              If a User is deleted, their posts will also be deleted (models.CASCADE).
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date'] # Optional: Order posts by most recent by default