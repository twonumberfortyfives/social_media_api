from rest_framework import viewsets, permissions, generics, mixins

from drf_spectacular.utils import extend_schema, OpenApiParameter

import application.permissions
from application.models import Post, Like, Comment, Follow
from application.serializers import (
    PostSerializer,
    LikeSerializer,
    LikeListSerializer,
    CommentSerializer,
    FollowSerializer,
    PostListSerializer,
    CommentListSerializer,
    FollowListSerializer,
    MyFollowersSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = self.queryset
        hashtag = self.request.query_params.get("hashtag")
        if self.action in ("list", "retrieve"):
            queryset = queryset.select_related("author").prefetch_related(
                "likes", "comments"
            )
        if hashtag:
            queryset = queryset.filter(hashtag__icontains=hashtag)
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="hashtag",
                description="filter posts by hashtag",
                type=str,
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class MyPostViewSet(PostViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        if self.request.user.is_authenticated:
            queryset = (
                queryset.select_related("author")
                .prefetch_related("likes")
                .filter(author=self.request.user)
            )
        return queryset


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.select_related("user", "post").filter(
            user=self.request.user
        )
        return queryset

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return LikeListSerializer
        return LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = queryset.select_related("user", "post").filter(
                user=self.request.user
            )
        return queryset

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return CommentListSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ("list", "retrieve"):
            queryset = queryset.select_related("following").filter(
                follower=self.request.user
            )
        return queryset

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return FollowListSerializer
        return FollowSerializer

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class MyFollowersViewSet(
    viewsets.ReadOnlyModelViewSet,
    mixins.DestroyModelMixin,
):
    queryset = Follow.objects.all()
    serializer_class = MyFollowersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(following=self.request.user).select_related("follower")
        return queryset
