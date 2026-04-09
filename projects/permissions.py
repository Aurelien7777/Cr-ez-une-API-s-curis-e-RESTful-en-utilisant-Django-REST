from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAuthorOrReadOnly(BasePermission):
    """
    Permission personnalisée :
    - Lecture autorisée à tous les utilisateurs authentifiés
    - Modification autorisée uniquement à l'auteur de l'objet
    """
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user