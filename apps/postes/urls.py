# departement/urls.py

from rest_framework.routers import DefaultRouter
from .views import DepartementViewSet, PosteViewSet

# Crée un routeur par défaut pour enregistrer les ViewSets
router = DefaultRouter()
# Enregistre DepartementViewSet avec le préfixe 'departements'
router.register(r'departements', DepartementViewSet)
# Enregistre PosteViewSet avec le préfixe 'postes'
router.register(r'postes', PosteViewSet)

# Les motifs d'URL sont générés automatiquement par le routeur
urlpatterns = router.urls