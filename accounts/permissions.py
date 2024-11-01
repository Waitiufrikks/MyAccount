from rest_framework import permissions
from accounts.models import Account

class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Verifica se o usuário autenticado é o dono da conta
        return obj.user == request.user