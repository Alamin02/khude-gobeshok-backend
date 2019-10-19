from django.contrib.auth.models import AbstractUser
from django.db import models
from contents.models import ProfileImage


# Create your models here.
class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Profile(models.Model):
    profile_owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.OneToOneField(ProfileImage, blank=True, null=True, on_delete=models.SET_NULL)
    full_name = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=150, blank=True)
    specialized_in = models.TextField(blank=True)
    software_skills = models.TextField(blank=True)
    phone_number = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.profile_owner.username


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institute = models.CharField(max_length=250)
    major = models.CharField(max_length=250)
    degree = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_enrolled = models.BooleanField()


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField()
