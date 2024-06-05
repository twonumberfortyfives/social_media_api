from django.urls import path, include
from rest_framework import routers

from application import views


app_name = "application"


router = routers.DefaultRouter()
router.register("my_posts", views.MyPostViewSet, basename="my-posts")
router.register(r"posts", views.PostViewSet)
router.register(r"comments", views.CommentViewSet)
router.register(r"likes", views.LikeViewSet)
router.register(r"follows", views.FollowViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
