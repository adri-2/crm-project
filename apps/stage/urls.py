# stage/urls.py

from django.urls import path
from .views import (
    StagiaireListCreateAPIView, StagiaireRetrieveUpdateDestroyAPIView,
    PeriodeStageListCreateAPIView, PeriodeStageRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # URLs pour Stagiaire
    path('stagiaires/', StagiaireListCreateAPIView.as_view(), name='stagiaire-list-create'),
    path('stagiaires/<int:pk>/', StagiaireRetrieveUpdateDestroyAPIView.as_view(), name='stagiaire-detail-update-delete'),

    # URLs pour PeriodeStage
    path('periodes-stage/', PeriodeStageListCreateAPIView.as_view(), name='periode-stage-list-create'),
    path('periodes-stage/<int:pk>/', PeriodeStageRetrieveUpdateDestroyAPIView.as_view(), name='periode-stage-detail-update-delete'),
]