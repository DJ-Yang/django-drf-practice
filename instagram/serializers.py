from rest_framework import serializers
from .models import Post

from django.contrib.auth import get_user_model

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ['username', 'email']

class PostSerializer(serializers.ModelSerializer):
  author_username = serializers.ReadOnlyField(source='author.username') # 직렬화를 우리가 원하는 룰로 하고 싶을때 시리얼라이즈를 이용하는 방법.
  # author = AuthorSerializer()
  class Meta:
    model = Post
    fields = [
      'pk',
      'message',
      'created_at',
      'updated_at',
      'author_username',
      'is_public',
      'ip',
    ]