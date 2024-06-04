from rest_framework import viewsets

from application.models import (
    Post,
    Like,
    Comment,
    Follow
)
from application.serializers import (
    PostSerializer,
    LikeSerializer,
    CommentSerializer,
    FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
