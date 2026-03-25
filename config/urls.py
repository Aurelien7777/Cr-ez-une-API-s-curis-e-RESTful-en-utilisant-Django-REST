from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from projects.views import ProjectViewSet, ContributorViewSet, IssueViewSet, CommentViewSet


# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Enregistre les routes CRUD de l'utilisateur
router.register('user', UserViewSet, basename='user')
router.register("projects", ProjectViewSet, basename="projects")
router.register("contributors", ContributorViewSet)
router.register("issues", IssueViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("", include("users.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Il faut bien penser à ajouter les urls du router dans la liste des urls disponibles.
    path('api/', include(router.urls)),
]
