from django.urls import path, include

from network_api.views import (
    UserViewSet,
    CreateUserView,
    PostViewSet,
    CreatePostView,
    LikePostView,
    UnlikePostView,
    AnalyticLikesView,
    AnalyticUserView,
)


urlpatterns = [
    path('users', UserViewSet.as_view({'get': 'list'})),
    path('users/signup', CreateUserView.as_view()),
    path('users/auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('posts', PostViewSet.as_view({'get': 'list'})),
    path('posts/create', CreatePostView.as_view()),
    path('posts/<int:pk>/like', LikePostView.as_view()),
    path('posts/<int:pk>/unlike', UnlikePostView.as_view()),

    path('analytics/likes', AnalyticLikesView.as_view()),
    path('analytics/user-activity', AnalyticUserView.as_view()),
]
