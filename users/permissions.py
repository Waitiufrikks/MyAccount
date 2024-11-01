from rest_framework import permissions
from rest_framework.views import Request


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        user_id = view.kwargs.get("user_id")
        user = request.user
        

        if not request.auth:
            return False
        if user.id == user_id:
            return True
      

        return False