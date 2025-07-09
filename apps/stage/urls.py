# stage/urls.py

from rest_framework.routers import DefaultRouter
from .views import StagiaireViewSet, PeriodeStageViewSet

# Crée un routeur par défaut pour enregistrer les ViewSets
router = DefaultRouter()
# Enregistre StagiaireViewSet avec le préfixe 'stagiaires'
router.register(r'stagiaires', StagiaireViewSet)
# Enregistre PeriodeStageViewSet avec le préfixe 'periodes-stage'
router.register(r'periodes-stage', PeriodeStageViewSet)

# Les motifs d'URL sont générés automatiquement par le routeur
urlpatterns = router.urls