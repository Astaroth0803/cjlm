from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Beneficiary, Activity, Event
from .serializers import BeneficiarySerializer, ActivitySerializer, EventSerializer, UserSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class BeneficiaryViewSet(viewsets.ModelViewSet):
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                models.Q(ci__icontains=search) |
                models.Q(first_name__icontains=search) |
                models.Q(last_name__icontains=search)
            )
        return queryset

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.prefetch_related('events').all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

# ----------------- PUBLIC ENDPOINTS -----------------
class PublicBeneficiaryViewSet(viewsets.ModelViewSet):
    """ Allows creating profiles and searching them publicly (for the attendance form) """
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer
    permission_classes = [AllowAny]
    http_method_names = ['get', 'post', 'head', 'options']

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                models.Q(ci__icontains=search) |
                models.Q(first_name__icontains=search) |
                models.Q(last_name__icontains=search)
            )
        return queryset

class PublicActivityViewSet(viewsets.ReadOnlyModelViewSet):
    """ Allows listing active activities and events for the public form """
    serializer_class = ActivitySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        today = timezone.now().date()
        return Activity.objects.filter(
            is_active=True
        ).exclude(
            category=Activity.Category.EVENTUAL,
            deadline_date__lt=today
        ).prefetch_related('events')
