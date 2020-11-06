from django.shortcuts import render

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

# 제네릭을 사용한 클래스 기반 뷰 구현
# class PublicPostListAPIView(generics.ListAPIView):
#   queryset = Post.objects.filter(is_public=True)
#   serializer_class = PostSerializer

# APIView를 이용해서 클래스 기반 뷰 직접 구현
# class PublicPostListAPIView(APIView):
#   def get(self, request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)

# public_post_lost = PublicPostListAPIView.as_view()

# 함수 기반 뷰
@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)
  


class PostViewSet(ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
