from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Beneficiary, Activity, Event

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'is_staff', 'is_active']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

class BeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary
        fields = '__all__'

    def validate_ci(self, value):
        if value == "":
            return None
        return value

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'name', 'category', 'deadline_date', 'description', 'is_active', 'image', 'events']
