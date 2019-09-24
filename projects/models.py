from django.db import models
from users.models import User
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    tags = models.CharField(max_length=120, blank=True)
    teammates = models.CharField(max_length=120, blank=True)
    thumbnail = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = JSONField()

    def __str__(self):
        return self.title
