from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if [IsAuthenticated]:
            return request.user == view.get_object().user
        return False
