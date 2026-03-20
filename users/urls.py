"""from django.urls import path,include
from rest_framework import routers
from . views import UserViewset"""

"""
# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/category/’
router.register('user', UserViewset, basename='user')
"""

"""urlpatterns = [
    path('api/', include(router.urls))  
    # Il faut bien penser à ajouter les urls du router dans la liste des urls disponibles.
]
"""
