from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # masque le mot de passe

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
            raise serializers.ValidationError(
                "Un utilisateur doit avoir au moins 15 ans."
            )
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        return user