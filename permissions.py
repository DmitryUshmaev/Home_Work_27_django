from rest_framework.permissions import BasePermission


class IsOwnerSelection(BasePermission):
    message = "Вы не являетесь владельцем данной подборки"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True

        return False
