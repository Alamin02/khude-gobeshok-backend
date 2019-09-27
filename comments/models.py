from django.db import models
from users.models import User


# Create your models here.
class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
