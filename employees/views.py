from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    """
    GET: List all departments
    POST: Create a new department
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['name']
    ordering_fields = ['name']

class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single department
    PUT/PATCH: Update it
    DELETE: Remove it
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

class EmployeeListCreateView(generics.ListCreateAPIView):
    """
    GET: List all employees
    POST: Create a new employee
    """
    queryset = Employee.objects.select_related('department').all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['department', 'date_of_joining']
    ordering_fields = ['date_of_joining', 'name']
    search_fields = ['name', 'email']

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single employee
    PUT/PATCH: Update it
    DELETE: Remove it
    """
    queryset = Employee.objects.select_related('department').all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

