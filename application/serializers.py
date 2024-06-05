import validators
from rest_framework import serializers, validators

from application.models import Post, Like, Comment, Follow


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("post",)

    def validate(self, data):
        request = self.context.get('request')
        user = request.user

        if Like.objects.filter(user=user, post=data['post']).exists():
            raise serializers.ValidationError("You can like only once.")

        return data


class LikeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("id", "post", "created_at", "user")


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="user.email"
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "content",
            "media",
            "created_at",
            "updated_at",
            "likes",
            "hashtag"
        )


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.email", read_only=True)
    likes = serializers.SerializerMethodField(method_name="get_amount_of_likes")

    class Meta:
        model = Post
        fields = (
            "id",
            "content",
            "media",
            "created_at",
            "updated_at",
            "author",
            "likes",
            "hashtag"
        )

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
