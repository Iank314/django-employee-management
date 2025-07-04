from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Performance
from .serializers import PerformanceSerializer

class PerformanceListCreateView(generics.ListCreateAPIView):
    """
    GET: List all Performance records (with filtering and ordering)
    POST: Create a new Performance record
    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['employee', 'rating', 'review_date']
    ordering_fields = ['review_date', 'rating']

class PerformanceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single Performance record
    PUT/PATCH: Update it
    DELETE: Remove it
    """
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAuthenticated]
