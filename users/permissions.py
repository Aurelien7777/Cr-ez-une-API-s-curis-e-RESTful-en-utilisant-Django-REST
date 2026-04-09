from rest_framework.permissions import BasePermission


class IsSelf(BasePermission):
    """
    Retourne "True" si l'objet utilisateur ciblé par la requête
    correspond à  l'utilisateur connecté
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user
