import os
import uuid

from django.db import models
from django.utils.text import slugify

from social_media_api.settings import AUTH_USER_MODEL


def post_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.author)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/post_pictures/", filename)


class Post(models.Model):
    author = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    content = models.TextField(max_length=500)
    media = models.FileField(upload_to=post_image_file_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)


class Follow(models.Model):
    follower = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers"
    )
    following = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following"
    )
    created_at = models.DateTimeField(auto_now_add=True)
