"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# my_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importe les vues de JWT pour les tokens
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView, # Optionnel, pour vérifier la validité d'un token
)

# Créez un routeur par défaut pour enregistrer vos ViewSets
router = DefaultRouter()
# Nous allons enregistrer les ViewSets dans les urls.py de chaque application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # Pour le login/logout via l'interface DRF (utile pour le débogage)

    # URLs pour l'authentification JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Pour obtenir un token d'accès et de rafraîchissement
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Pour rafraîchir un token d'accès
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),   # Optionnel: Pour vérifier la validité d'un token

    # Inclut les URLs de chaque application via un préfixe 'api/'
    path('api/', include('apps.users.urls')),
    # path('api/', include('departement.urls')),
    path('api/', include('apps.postes.urls')),
    # path('api/', include('apps.employees.urls')),
    path('api/', include('apps.stage.urls')),
    path('api/', include('apps.recruitment.urls')),
]