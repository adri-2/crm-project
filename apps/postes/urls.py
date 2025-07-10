# postes/urls.py

from django.urls import path
from .views import (
    DepartementListCreateAPIView, DepartementRetrieveUpdateDestroyAPIView,
    CompetenceListCreateAPIView, CompetenceRetrieveUpdateDestroyAPIView,
    PosteListCreateAPIView, PosteRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # URLs pour Departement (maintenant dans l'app postes)
    path('departements/', DepartementListCreateAPIView.as_view(), name='departement-list-create'),
    path('departements/<int:pk>/', DepartementRetrieveUpdateDestroyAPIView.as_view(), name='departement-detail-update-delete'),

    # URLs pour Competence
    path('competences/', CompetenceListCreateAPIView.as_view(), name='competence-list-create'),
    path('competences/<int:pk>/', CompetenceRetrieveUpdateDestroyAPIView.as_view(), name='competence-detail-update-delete'),

    # URLs pour Poste
    path('postes/', PosteListCreateAPIView.as_view(), name='poste-list-create'),
    path('postes/<int:pk>/', PosteRetrieveUpdateDestroyAPIView.as_view(), name='poste-detail-update-delete'),
]