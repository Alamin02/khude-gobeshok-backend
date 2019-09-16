from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize


# Create your models here.
class ThumbnailImage(models.Model):
    image = models.ImageField(upload_to="images/")
    thumbnail = ImageSpecField(source='image',
                                      processors=[SmartResize(300, 225)],
                                      format='JPEG',
                                      options={'quality': 60},)


class ImageContent(models.Model):
    image = models.ImageField(upload_to="images/")
    caption = models.CharField(blank=True, max_length=120)


class ProfileImage(models.Model):
    image = models.ImageField(upload_to="images/")
    thumbnail = ImageSpecField(source='image',
                               processors=[SmartResize(300, 300)],
                               format='JPEG',
                               options={'quality': 60}, )
