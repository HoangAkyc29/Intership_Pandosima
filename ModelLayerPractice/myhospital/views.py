from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
import django.contrib.auth.models
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Doctor, Patient, Appointment, PrescriptionLines
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, PrescriptionLinesSerializer, UserSerializer, UserLoginSerializer
from .models import MyUser



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
            if user:
                token, created = Token.objects.get_or_create(user=user)
                # refresh = TokenObtainPairSerializer.get_token(user)
                data = {"access_token": str(token), "user_id": str(user.id)}
                return Response(data, status=status.HTTP_200_OK)

        return Response(
            {"error_message": "Email or password is incorrect!", "error_code": 400},
            status=status.HTTP_400_BAD_REQUEST,
        )


class RegisterView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.validated_data("password")
            user = serializer.save()
            # user= MyUser.objects.create_user(email=request.data.username, password=request.data.password)
            # user.save();
            # return Response(request.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                {"message": "Register successful!"}, status=status.HTTP_201_CREATED
            )
        else:
            return JsonResponse(
                {
                    "error_message": "This email has already exist!",
                    "errors_code": 400,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class DoctorListView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return Doctor.objects.filter(name__icontains=search_query)
        return Doctor.objects.all()

class DoctorDetailView(RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientListView(ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return Patient.objects.filter(name__icontains=search_query)
        return Patient.objects.all()

class PatientDetailView(RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class AppointmentListView(ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return Appointment.objects.filter(name__icontains=search_query)
        return Appointment.objects.all()

class AppointmentPatientView(ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]

    serializer_class = AppointmentSerializer

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')
        return Appointment.objects.filter(patient__id=patient_id)

class AppointmentDoctorView(ListAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')
        return Appointment.objects.filter(doctor__id=doctor_id)

class AppointmentDetailView(RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Lấy danh sách PrescriptionLines tương ứng với appointment
        prescription_lines = PrescriptionLines.objects.filter(appointment=instance)
        prescription_lines_serializer = PrescriptionLinesSerializer(prescription_lines, many=True)

        # Thêm danh sách PrescriptionLines vào dữ liệu serialized để trả về
        data = serializer.data
        data['prescription_lines'] = prescription_lines_serializer.data

        return Response(data)
