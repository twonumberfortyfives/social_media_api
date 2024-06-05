from rest_framework import serializers

from application.models import Post, Like, Comment, Follow


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("content", "media", "created_at", "updated_at")


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.email", read_only=True)

    class Meta:
        model = Post
        fields = ("content", "media", "created_at", "updated_at", "author")


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "post",
            "content",
            "created_at",
        )


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Comment
        fields = ("user", "post", "content", "created_at")


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"
