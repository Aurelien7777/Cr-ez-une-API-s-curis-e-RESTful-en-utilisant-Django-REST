from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Permet de convertir les données JSON
    en objets Django et inversement.
    Assure la validation des données,
    notamment de l'âge minimum,
    et gère la création des utilisateurs
    avec un mot de passe hashé
    via la méthode create_user.
    """

    # masque le mot de passe dans les communications
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "age",
            "can_be_contacted",
            "can_data_be_shared",
        ]

    def validate_age(self, value):
        """
        Fonction visant à vérifier l'age de l'utilisateur
        lors de son inscription
        """
        if value < 15:
            raise serializers.ValidationError("Un utilisateur doit avoir au moins 15 ans.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user
