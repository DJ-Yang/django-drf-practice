from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet)


urlpatterns = [
    path('public/', views.PostListAPIView.as_view()),
    path('', include(router.urls)),
]
