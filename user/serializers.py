from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    followings = serializers.SerializerMethodField(method_name="get_following")
    followers = serializers.SerializerMethodField(method_name="get_followers")

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "bio",
            "password",
            "profile_picture",
            "followings",
            "followers",
        )
        read_only_fields = (
            "date_joined",
            "last_login",
            "is_staff",
            "is_superuser",
            "id",
        )
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8, "max_length": 255},
        }

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update user with encrypted password."""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user

    def get_following(self, obj):
        return obj.followers.count()

    def get_followers(self, obj):
        return obj.following.count()
