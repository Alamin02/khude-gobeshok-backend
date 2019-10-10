from django.db import models
from users.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Notification(models.Model):
    INFO = 'i'
    SUCCESS = 's'
    WARNING = 'w'
    ERROR = 'e'
    LEVELS = [
        (INFO, 'info'),
        (SUCCESS, 'success'),
        (WARNING, 'warning'),
        (ERROR, 'error')
    ]

    level = models.CharField(choices=LEVELS, default=LEVELS[0], max_length=20)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    unread = models.BooleanField(default=True, blank=False, db_index=True)

    actor_content_type = models.ForeignKey(ContentType, related_name='actor', on_delete=models.CASCADE)
    actor_object_id = models.PositiveIntegerField()
    actor = GenericForeignKey('actor_content_type', 'actor_object_id')

    verb = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)

    target_content_type = models.ForeignKey(
        ContentType,
        related_name='target',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')

    action_object_content_type = models.ForeignKey(
        ContentType,
        related_name='action_object',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    action_object_object_id = models.PositiveIntegerField(null=True, blank=True,)
    action_object = GenericForeignKey('action_object_content_type', 'action_object_object_id')

    timestamp = models.DateTimeField(auto_now_add=True)
