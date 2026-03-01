from rest_framework import serializers
from .models import AttendanceRecord
from core.serializers import BeneficiarySerializer, EventSerializer

class AttendanceRecordSerializer(serializers.ModelSerializer):
    beneficiary_details = BeneficiarySerializer(source='beneficiary', read_only=True)
    event_details = EventSerializer(source='event', read_only=True)

    class Meta:
        model = AttendanceRecord
        fields = ['id', 'beneficiary', 'event', 'date', 'recorded_by', 'beneficiary_details', 'event_details']
        read_only_fields = ['recorded_by', 'date']
