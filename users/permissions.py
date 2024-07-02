from rest_framework import permissions


class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='manager').exists()


class IsNotManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.groups.filter(name='manager').exists()
