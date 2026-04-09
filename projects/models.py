from django.conf import settings
from django.db import models
import uuid


class Project(models.Model):
    """
    Représente un projet.
    - Contient les informations principales 
    (titre, description, type)
    - Lié à un auteur (utilisateur)
    - Date de création automatique
    """
    
    BACKEND = "BACK-END"
    FRONTEND = "FRONT-END"
    IOS = "IOS"
    ANDROID = "ANDROID"

    TYPE_CHOICES = [
        (BACKEND, "Back-end"),
        (FRONTEND, "Front-end"),
        (IOS, "iOS"),
        (ANDROID, "Android"),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="authored_projects",
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    """
    Représente un contributeur d’un projet.
    - Associe un utilisateur à un projet
    - Empêche les doublons (user, project)
    - Date d’ajout automatique
    """
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributions",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="contributors",
    )
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "project")

    def __str__(self):
        return f"{self.user.username} - {self.project.title}"



class Issue(models.Model):
    """
    Représente une issue (ticket) d’un projet.
    - Contient description, priorité, statut et type
    - Liée à un projet, un auteur et 
      éventuellement un assignee
    - Date de création automatique
    """
    
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

    PRIORITY_CHOICES = [
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    ]

    BUG = "BUG"
    FEATURE = "FEATURE"
    TASK = "TASK"

    TAG_CHOICES = [
        (BUG, "Bug"),
        (FEATURE, "Feature"),
        (TASK, "Task"),
    ]

    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"

    STATUS_CHOICES = [
        (TODO, "To Do"),
        (IN_PROGRESS, "In Progress"),
        (FINISHED, "Finished"),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField()
    tag = models.CharField(max_length=20, choices=TAG_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=TODO
    )

    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="issues",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="authored_issues",
    )

    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_issues",
    )

    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Représente un commentaire sur une issue.
    - Identifié par un UUID
    - Lié à un auteur et une issue
    - Date de création automatique
    """
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    description = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

