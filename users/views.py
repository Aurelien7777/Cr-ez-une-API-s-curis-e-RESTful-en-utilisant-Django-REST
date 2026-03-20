from users.serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from .models import User
from rest_framework.permissions import IsAuthenticated

class UserViewSet(ModelViewSet):
    
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()

