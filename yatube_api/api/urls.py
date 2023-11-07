from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import CommentModelViewSet, GroupModelViewSet, PostModelViewSet

router = SimpleRouter()
router.register(r'groups', GroupModelViewSet)
router.register(r'posts', PostModelViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentModelViewSet, basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
