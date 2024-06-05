import validators
from rest_framework import serializers, validators

from application.models import Post, Like, Comment, Follow


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("post", "created_at")


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="user.email"
    )

    class Meta:
        model = Post
        fields = ("content", "media", "created_at", "updated_at", "likes")


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.email", read_only=True)
    likes = serializers.SerializerMethodField(method_name="get_amount_of_likes")

    class Meta:
        model = Post
        fields = ("content", "media", "created_at", "updated_at", "author", "likes")

    def get_amount_of_likes(self, obj) -> int:
        return obj.likes.count()


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
