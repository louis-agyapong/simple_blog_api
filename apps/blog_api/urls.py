from django.urls import path
from .views import PostDetail, PostList

app_name = "blog_api"

urlpatterns = [
    path("blog/", PostList.as_view(), name="list_create"),
    path("blog/<int:pk>/", PostDetail.as_view(), name="detail_create"),
]
