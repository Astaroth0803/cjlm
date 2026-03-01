from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import AttendanceRecord
from .serializers import AttendanceRecordSerializer

class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all().select_related('beneficiary', 'event')
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(recorded_by=self.request.user)


class PublicAttendanceViewSet(viewsets.ModelViewSet):
    """ Allows anyone to register attendance on the public form """
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post', 'options']

    def perform_create(self, serializer):
        # Let 'recorded_by' be null because it's a public self-registration
        serializer.save()
