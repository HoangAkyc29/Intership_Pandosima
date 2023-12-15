from django.urls import path
from .views import (
    DoctorListView,
    DoctorDetailView,
    PatientListView,
    PatientDetailView,
    AppointmentListView,
    AppointmentPatientView,
    AppointmentDoctorView,
    AppointmentDetailView,
    UserViewSet,
    LoginView,
    RegisterView
)
app_name = 'myhospital'

user_list = UserViewSet.as_view({"get": "list"})
user_detail = UserViewSet.as_view({"get": "retrieve"})


urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),

    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),

    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/patient/<int:patient_id>/', AppointmentPatientView.as_view(), name='appointment_patient_list'),
    path('appointments/doctor/<int:doctor_id>/', AppointmentDoctorView.as_view(), name='appointment_doctor_list'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path("users/", user_list, name="user-list"),
    path("users/<int:pk>/", user_detail, name="user-detail"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
]
