from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import User
from .permissions import IsSelf
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    ViewSet gérant les opérations API liées aux utilisateurs.
    Cette vue orchestre les actions CRUD en utilisant le serializer
    pour valider et transformer les données. Elle limite l'accès aux
    objets via get_queryset et contrôle les autorisations avec
    get_permissions.
    """

    serializer_class = UserSerializer

    def get_queryset(self):
        """
        sert à définir quels objets de la base
        cette vue est autorisée à manipuler / consulter
        """
        return User.objects.filter(id=self.request.user.id)

    def get_permissions(self):
        """
        Permet de définir les autorisations
        en fonction des actions à effectuer
        """
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated(), IsSelf()]
