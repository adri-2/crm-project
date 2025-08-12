# employees/urls.py

from django.urls import path
from .views import EmployeListCreateAPIView, EmployeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('employes/', EmployeListCreateAPIView.as_view(), name='employe-list-create'),
    path('employes/<int:pk>/', EmployeRetrieveUpdateDestroyAPIView.as_view(), name='employe-detail-update-delete'),
]