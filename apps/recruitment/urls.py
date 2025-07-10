# recruitment/urls.py

from django.urls import path
from .views import (
    OffreEmploiListCreateAPIView, OffreEmploiRetrieveUpdateDestroyAPIView,
    CandidatListCreateAPIView, CandidatRetrieveUpdateDestroyAPIView,
    CandidatAcceptAPIView, CandidatRejectAPIView
)

urlpatterns = [
    # URLs pour OffreEmploi
    path('offres-emploi/', OffreEmploiListCreateAPIView.as_view(), name='offre-emploi-list-create'),
    path('offres-emploi/<int:pk>/', OffreEmploiRetrieveUpdateDestroyAPIView.as_view(), name='offre-emploi-detail-update-delete'),

    # URLs pour Candidat
    path('candidats/', CandidatListCreateAPIView.as_view(), name='candidat-list-create'),
    path('candidats/<int:pk>/', CandidatRetrieveUpdateDestroyAPIView.as_view(), name='candidat-detail-update-delete'),
    path('candidats/<int:pk>/accept/', CandidatAcceptAPIView.as_view(), name='candidat-accept'), # Action personnalisée
    path('candidats/<int:pk>/reject/', CandidatRejectAPIView.as_view(), name='candidat-reject'), # Action personnalisée
]