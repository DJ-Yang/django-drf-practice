from django.db import models
from django.conf import settings

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  message = models.TextField()
  created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
  updated_at = models.DateTimeField( auto_now=True, auto_now_add=False)
