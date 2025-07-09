# employees/urls.py

from rest_framework.routers import DefaultRouter
from .views import EmployeViewSet

# Crée un routeur par défaut pour enregistrer les ViewSets
router = DefaultRouter()
# Enregistre EmployeViewSet avec le préfixe 'employes'
router.register(r'employes', EmployeViewSet)

# Les motifs d'URL sont générés automatiquement par le routeur
urlpatterns = router.urls