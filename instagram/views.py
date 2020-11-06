from django.shortcuts import render

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

class PostListAPIView(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
