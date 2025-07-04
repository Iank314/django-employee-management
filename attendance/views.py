from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceListCreateView(generics.ListCreateAPIView):
    """
    GET: List all Attendance records (filterable by employee, date, status)
    POST: Create a new Attendance record
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['employee', 'date', 'status']
    ordering_fields = ['date']

class AttendanceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a single Attendance record
    PUT/PATCH: Update it
    DELETE: Remove it
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
