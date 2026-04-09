from rest_framework import serializers
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer des projets.
    - Champs principaux du modèle Project
    - author et created_time en lecture seule
    """
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author",
            "created_time",
        ]
        read_only_fields = ["author", "created_time"]


class ContributorSerializer(serializers.ModelSerializer):
    """
    Serializer des contributeurs.
    - Associe un utilisateur à un projet
    - created_time en lecture seule
    """
    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "created_time"]
        read_only_fields = ["created_time"]


class IssueSerializer(serializers.ModelSerializer):
    """
    Serializer des issues.
    - Champs principaux d'une issue
    - author et created_time en lecture seule
    """
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "status",
            "project",
            "author",
            "assignee",
            "created_time",
        ]
        read_only_fields = ["author", "created_time"]


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer des commentaires.
    - Champs principaux d'un commentaire lié à une issue
    - author et created_time en lecture seule
    """
    class Meta:
        model = Comment
        fields = [
            "id",
            "description",
            "author",
            "issue",
            "created_time",
        ]
        read_only_fields = ["author", "created_time"]