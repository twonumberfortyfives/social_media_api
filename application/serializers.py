import validators
from rest_framework import serializers, validators

from application.models import Post, Like, Comment, Follow
from user.serializers import UserSerializer


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
            "hashtag",
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "post",
            "content",
        )


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Comment
        fields = ("user", "post", "content", "created_at")


class CommentForPostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.email", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "user", "content", "created_at")


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.email", read_only=True)
    likes = serializers.SerializerMethodField(method_name="get_amount_of_likes")
    comments = CommentForPostSerializer(many=True, read_only=True)

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
            "hashtag",
            "comments"
        )

    def get_amount_of_likes(self, obj) -> int:
        return obj.likes.count()


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ("following",)

    def validate(self, data):
        request = self.context.get('request')
        user = request.user
        if data["following"] == user:
            raise serializers.ValidationError("You can't follow yourself.")
        if Follow.objects.filter(follower=user, following=data["following"]).exists():
            raise serializers.ValidationError("You can't follow twice")
        return data


class FollowListSerializer(serializers.ModelSerializer):
    following = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ("id", "following", "created_at",)


class MyFollowersSerializer(serializers.ModelSerializer):
    follower = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ("id", "follower", "created_at",)
