from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission, SAFE_METHODS


class BasePermissionWithGroup(BasePermission):
    def is_user_admin(self, user):
        if isinstance(user, AnonymousUser):
            return False
        return 'admin' in map(str, user.groups.all())

class IsAdminOrReadOnly(BasePermissionWithGroup):
    def has_permission(self, request, view):
        return (self.is_user_admin(request.user)
                or
                request.method in SAFE_METHODS)
    def has_object_permission(self, request, view, obj):
        return (self.is_user_admin(request.user)
                or
                request.method in SAFE_METHODS)

class UserPermission(BasePermissionWithGroup):
    def has_permission(self, request, view):
        # могут смотреть только зарегистрированные
        # могут изменять только пользователи из группы admin
        return ((request.method in SAFE_METHODS and not isinstance(request.user, AnonymousUser))
                or
                self.is_user_admin(request.user))

    def has_object_permission(self, request, view, obj):
        # смотреть пользователя может либо пользователь либо админ
        # менять только админ
        return (request.method in SAFE_METHODS and request.user.pk == obj.pk
                or
                self.is_user_admin(request.user))