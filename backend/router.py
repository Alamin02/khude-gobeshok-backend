from rest_framework.routers import DefaultRouter
from projects.views import ProjectViewSet
from comments.views import CommentViewSet

router = DefaultRouter()

router.register(r'projects', ProjectViewSet, base_name='projects')
router.register(r'comments', CommentViewSet, base_name='comments')
