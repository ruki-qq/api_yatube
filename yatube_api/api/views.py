from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.permissions import IsAuthenticatedAuthorOrReadOnly
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class PostModelViewSet(viewsets.ModelViewSet):
    """Provides CRUD for posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Provides 'read-only' actions for groups."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentModelViewSet(viewsets.ModelViewSet):
    """Provides CRUD for comments."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedAuthorOrReadOnly,)

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
