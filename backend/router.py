from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet
from comments.views import CommentViewSet
from directmessages.views import ConversationViewSet
from notifications.views import NotificationViewSet
from users.views import SquadViewSet
from company.views import ContactUsViewSet

router = DefaultRouter()

router.register(r'projects', ProjectViewSet, base_name='projects')
router.register(r'comments', CommentViewSet, base_name='comments')
router.register(r'conversations', ConversationViewSet, base_name='conversations')
router.register(r'notifications', NotificationViewSet, base_name='notifications')
router.register(r'squads', SquadViewSet, base_name='squads')
router.register(r'contact-us', ContactUsViewSet, base_name='contact_us')
