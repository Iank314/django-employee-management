from django.urls import path
from .views import (
    DepartmentListCreateView,
    DepartmentRetrieveUpdateDestroyView,
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView
)

urlpatterns = [
    # Department endpoints
    path('departments/', DepartmentListCreateView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyView.as_view(), name='department-detail'),
    # Employee endpoints
    path('', EmployeeListCreateView.as_view(), name='employee-list'),
    path('<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
]