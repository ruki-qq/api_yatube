from rest_framework import viewsets

from .permissions import IsAuthorOrReadOnly
from .serializers import GroupSerializer, PostSerializer
from posts.models import Comment, Group, Post


class PostModelViewSet(viewsets.ModelViewSet):
    """Provides CRUD for posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Provides 'read-only' actions for groups."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentModelViewSet(viewsets.ModelViewSet):
    pass
