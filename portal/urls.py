#from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView, PostDetailedView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='portal-homepage'),
    path('post/<int:pk>/', PostDetailedView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='portal-about'),
    ]