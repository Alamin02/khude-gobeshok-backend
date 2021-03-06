from django.db.models.signals import post_save
from django.dispatch import receiver
from comments.models import Comment
from notifications.models import Notification


@receiver(post_save, sender=Comment, dispatch_uid="comment_save_receiver")
def notify_comment(sender, instance, **kwargs):
    comment_notification = Notification(
        level=Notification.INFO,
        recipient=instance.project.author,
        verb="commented on",
        actor=instance.commenter,
        target=instance.project
    )
    comment_notification.save()
    pass
