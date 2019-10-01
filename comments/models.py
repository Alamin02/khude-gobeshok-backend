from django.db import models
from users.models import User
from projects.models import Project


# Create your models here.
class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
