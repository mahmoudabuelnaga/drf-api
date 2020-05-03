from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework import generics
import django_filters.rest_framework
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.


class PostViewSets(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # def list(self, request):
    #     queryset = Post.objects.all()
    #     serializer = PostSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     queryset = Post.objects.all()
    #     serializer = PostSerializer()
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     # queryset = Post.objects.all()
    #     qs = get_object_or_404(Post, pk=pk)
    #     serializer = PostSerializer(qs)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     queryset = get_object_or_404(Post, pk=pk)
    #     serilaizer = PostSerializer(queryset)
    #     if serilaizer.is_valid():
    #         serilaizer.save()
    #         return Response(serilaizer.data)


class PostAPIView2(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # pagination_class = 1
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['title', 'owner']

    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.objects = self.get_queryset
        return Response({'posts': self.objects}, template_name='post.html')

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = PostSerializer(queryset, many=True)
    #     return Response(serializer.data)


class PostAPIView3(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostListCreateAPIView4(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetreiveUpdateDestroyAPIView4(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# APIView


class ListUser(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        username = [user.username for user in User.objects.all()]
        return Response(username)


class PostAPIView(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  generics.GenericAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     return destroy(request, *args, **kwargs)


# class TestView(APIView):

#     permission_classes = (permissions.IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
