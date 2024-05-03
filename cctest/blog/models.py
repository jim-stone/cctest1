from django.db import models

from cctest.users.models import User

# Create your models here.


class Post:
    title = models.CharField(max_length=2000)
    content = models.CharField(max_length=10000)
    published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
