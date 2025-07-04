from django.urls import path
from .views import (
    PerformanceListCreateView,
    PerformanceRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', PerformanceListCreateView.as_view(), name='performance-list'),
    path('<int:pk>/', PerformanceRetrieveUpdateDestroyView.as_view(), name='performance-detail'),
]