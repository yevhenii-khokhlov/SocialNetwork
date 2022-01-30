from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title')
    text = models.TextField(blank=True, null=True, verbose_name='Text')
    creation_date = models.DateTimeField(auto_created=True, verbose_name='Creation date')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')

    def __str__(self):
        return f"Post {self.id}"


class Like(models.Model):
    by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Like {self.id}"
