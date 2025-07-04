from django.urls import path
from .views import (
    AttendanceListCreateView,
    AttendanceRetrieveUpdateDestroyView
)

urlpatterns = [
    path('', AttendanceListCreateView.as_view(), name='attendance-list'),
    path('<int:pk>/', AttendanceRetrieveUpdateDestroyView.as_view(), name='attendance-detail'),
]
