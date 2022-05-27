from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, pagination, permissions, viewsets

from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from posts.models import Comment, Group, Post, Follow


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, )

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post_id)
        return comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class FollowsViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet
                     ):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username']

    def get_queryset(self):
        user = self.request.user
        follows = Follow.objects.filter(user=user)
        return follows

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
