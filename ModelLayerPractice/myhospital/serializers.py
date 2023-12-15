# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Patient, Doctor, Appointment, PrescriptionLines, MyUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name="snippet-detail", read_only=True
    )

    class Meta:
        model = MyUser
        fields = ["username", "email", "snippets"]


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class PrescriptionLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionLines
        fields = '__all__'
