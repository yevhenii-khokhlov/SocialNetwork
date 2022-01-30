from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView

from network_api.models import Post, Like
from network_api.serializers import (
    UserSerializer,
    PostSerializer,
    LikeSerializer,
)


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class CreatePostView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]


class LikePostView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    authentication_classes = [TokenAuthentication]


class UnlikePostView(DestroyAPIView):
    pass


class AnalyticLikesView(APIView):
    pass


class AnalyticUserView(APIView):
    pass


# user login
# post creation
# post like
# post unlike
# analytics about how many likes was made.
#       Example url:
#       /api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics
#       aggregated by day.
# user activity an endpoint which will show when user was login last time and when he mades a last request to the service.