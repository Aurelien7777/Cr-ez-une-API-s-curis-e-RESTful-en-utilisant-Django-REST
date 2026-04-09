from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthorOrReadOnly
from .models import Project, Contributor, Issue, Comment
from .serializers import (
    ProjectSerializer,
    ContributorSerializer,
    IssueSerializer,
    CommentSerializer,
)


class ProjectViewSet(ModelViewSet):
    """
    Gestion des projets (CRUD).
    - Accès : projets où l'utilisateur est contributeur
    - Permissions : authentifié + auteur pour modifier
    - Création : assigne l'auteur et l'ajoute comme contributeur
    """

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        """
        Définit quels objets de la base
        cette vue est autorisée à manipuler / consulter
        """
        return Project.objects.filter(contributors__user=self.request.user)

    def perform_create(self, serializer):
        """
        Ajoute l'utilisateur effectuant la création
        comme l'auteur ainsi que le contributeur
        """
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(user=self.request.user, project=project)


class ContributorViewSet(ModelViewSet):
    """
    Gestion des contributeurs (CRUD).
    - Accès : contributeurs des projets où l'utilisateur participe
    - Permissions : authentifié
    - Création : uniquement si l'utilisateur est déjà contributeur du projet
    """

    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        La fonction détermine
        quels objets Contributor
        l’utilisateur connecté a le droit
        de voir ou manipuler
        """
        return Contributor.objects.filter(project__contributors__user=self.request.user)

    def perform_create(self, serializer):
        project = serializer.validated_data["project"]

        # Vérifie que l'utilisateur est déjà contributeur du projet
        if not Contributor.objects.filter(project=project, user=self.request.user).exists():
            raise PermissionDenied("Vous n'êtes pas contributeur de ce projet.")

        serializer.save()


class IssueViewSet(ModelViewSet):
    """
    Gestion des issues (CRUD).

    - Accès : issues des projets où l'utilisateur est contributeur
    - Permissions : authentifié + auteur pour modifier
    - Création : utilisateur et assignee doivent être contributeurs,
    auteur assigné automatiquement
    """

    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Issue.objects.filter(project__contributors__user=self.request.user)

    def perform_create(self, serializer):
        project = serializer.validated_data["project"]

        # Vérifie que l'utilisateur est contributeur
        if not Contributor.objects.filter(project=project, user=self.request.user).exists():
            raise PermissionDenied("Vous n'êtes pas contributeur de ce projet.")

        # Vérifie que l'assignee est contributeur
        assignee = serializer.validated_data.get("assignee")

        if assignee and not Contributor.objects.filter(project=project, user=assignee).exists():
            raise PermissionDenied("L'assignee doit être contributeur du projet.")

        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    """
    Gestion des commentaires (CRUD).

    - Accès : commentaires liés aux projets où l'utilisateur est contributeur
    - Permissions : authentifié + auteur pour modifier
    - Création : uniquement si contributeur du projet, auteur assigné automatiquement
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(issue__project__contributors__user=self.request.user)

    def perform_create(self, serializer):
        issue = serializer.validated_data["issue"]

        # Vérifie que l'utilisateur est contributeur du projet lié à l'issue
        if not Contributor.objects.filter(project=issue.project, user=self.request.user).exists():
            raise PermissionDenied("Vous n'êtes pas contributeur de ce projet.")

        serializer.save(author=self.request.user)
