# recruitment/urls.py

from rest_framework.routers import DefaultRouter
from .views import OffreEmploiViewSet, CandidatViewSet

# Crée un routeur par défaut pour enregistrer les ViewSets
router = DefaultRouter()
# Enregistre OffreEmploiViewSet avec le préfixe 'offres-emploi'
router.register(r'offres-emploi', OffreEmploiViewSet)
# Enregistre CandidatViewSet avec le préfixe 'candidats'
router.register(r'candidats', CandidatViewSet)

# Les motifs d'URL sont générés automatiquement par le routeur
urlpatterns = router.urls