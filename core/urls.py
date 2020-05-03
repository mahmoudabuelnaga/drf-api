from django.urls import path, include
from .views import (PostAPIView, ListUser,
                    PostAPIView2, PostAPIView3,
                    PostListCreateAPIView4,
                    PostRetreiveUpdateDestroyAPIView4,
                    PostViewSets,
                    )
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'post', PostViewSets, basename='post')


urlpatterns = [
    path('', PostAPIView.as_view()),
    path('user/', ListUser.as_view()),
    path('post2/', PostAPIView2.as_view()),
    path('post3/', PostAPIView3.as_view()),
    # path('post4/', PostAPIView4.as_view()),
    path('post4/', PostListCreateAPIView4.as_view()),
    path('post4/<int:pk>/', PostRetreiveUpdateDestroyAPIView4.as_view()),

    path('', include(router.urls)),


]
