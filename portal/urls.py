#from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from .views import PostListView, PostDetailedView, PostCreateView, PostUpdateView, PostDeleteView
from .api import PostResource, ProfileResource, UserResource
from tastypie.api import Api

api_v1 = Api(api_name='v1')
api_v1.register(ProfileResource()) #.../api/v1/profile/
api_v1.register(PostResource())    #.../api/v1/post/
api_v1.register(UserResource())    #.../api/v1/post/

urlpatterns = [
    path('', PostListView.as_view(), name='portal-homepage'),
    path('post/<int:pk>/', PostDetailedView.as_view(), name='post-detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='portal-about'),
    path('test/', views.testVue, name='test-vue'),
    url(r'^api/', include(api_v1.urls)),
    ]