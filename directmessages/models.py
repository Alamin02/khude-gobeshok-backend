from django.db import models
from users.models import User

from django.db.models import F, When, Case


class MessageManager(models.Manager):
    def latest_distinct(self):
        return super().get_queryset().annotate(
            user_1=Case(
                When(sender__id__gt=F('recipient'), then=F('recipient')),
                default=F('sender')
            ),
            user_2=Case(
                When(sender__id__gt=F('recipient'), then=F('sender')),
                default=F('recipient')
            )
        ).order_by('user_1', 'user_2', '-sent_at').distinct('user_1', 'user_2')


# Create your models here.
class DirectMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    seen_at = models.DateTimeField(null=True, blank=True)

    objects = MessageManager()

    def __str__(self):
        return f'[{self.sent_at.ctime()}] {self.sender} -> {self.recipient}'

    class Meta:
        ordering = ['-sent_at']
