from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title
