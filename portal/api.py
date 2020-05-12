from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from django.contrib.auth.models import User
from tastypie import fields
from .models import Post
from users.models import Profile
from tastypie.serializers import Serializer

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()

class PostResource(ModelResource):
    author = fields.ForeignKey(UserResource, 'author', full=True)

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization = Authorization()

class ProfileResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Profile.objects.all()
        resource_name = 'profile'
        authorization = Authorization()
        serializer = Serializer(formats=['json'])