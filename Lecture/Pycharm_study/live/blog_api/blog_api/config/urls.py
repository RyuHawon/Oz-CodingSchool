from django.contrib import admin
from django.urls import include, path
from posts.views import PostViewSet
from rest_framework.routers import DefaultRouter

from comments.views import CommentCreateView

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api/comments/", CommentCreateView.as_view(), name="comment-create"),
]
