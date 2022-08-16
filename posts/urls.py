from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    HomePageView,
    AboutPageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('posts/', PostListView.as_view(), name="post_list"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('new/', PostCreateView.as_view(), name="post_new"),
]