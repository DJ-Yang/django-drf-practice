from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
  # 인증이 되어야만 목록조회/포스팅 허용
  def has_permission(self, request, view):
    return request.uesr and request.user.is_authenticated

  def has_objects_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    
    return obj.author == request.user