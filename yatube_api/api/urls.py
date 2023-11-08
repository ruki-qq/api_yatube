from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.views import CommentModelViewSet, GroupModelViewSet, PostModelViewSet

router_v1 = DefaultRouter()
router_v1.register('groups', GroupModelViewSet, basename='group')
router_v1.register('posts', PostModelViewSet, basename='post')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentModelViewSet, basename='comment'
)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
