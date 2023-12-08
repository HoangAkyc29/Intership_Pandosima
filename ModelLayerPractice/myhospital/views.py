from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Doctor, Patient, Appointment, PrescriptionLines



class DoctorListView(ListView):
    model = Doctor
    template_name = 'hospital/doctor_list.html'
    context_object_name = 'doctor_list'

    def get_queryset1(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return Doctor.objects.filter(name__icontains=search_query)
        return Doctor.objects.all()

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'hospital/doctor_detail.html'

class PatientListView(ListView):
    model = Patient
    template_name = 'hospital/Patient_list.html'
    context_object_name = 'patient_list'

    def get_queryset1(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return Patient.objects.filter(name__icontains=search_query)
        return Patient.objects.all()

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'hospital/patient_detail.html'

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'hospital/Appointment_list.html'
    context_object_name = 'appointment_list'

    def get_queryset1(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return Appointment.objects.filter(name__icontains=search_query)
        return Appointment.objects.all()

class AppointmentPatientView(ListView):
    model = Appointment
    template_name = 'hospital/appointment_patient_list.html'  # Đặt tên template của bạn
    context_object_name = 'appointment_list'

    def get_queryset(self):
        patient_id = self.kwargs.get('patient_id')  # Lấy ID của bệnh nhân từ đường dẫn
        return Appointment.objects.filter(patient__id=patient_id)

class AppointmentDoctorView(ListView):
    model = Appointment
    template_name = 'hospital/appointment_doctor_list.html'  # Đặt tên template của bạn
    context_object_name = 'appointment_list'

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')  # Lấy ID của bác sĩ từ đường dẫn
        return Appointment.objects.filter(doctor__id=doctor_id)

class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'hospital/appointment_detail.html'  # Đặt tên template của bạn
    context_object_name = 'appointment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        appointment = self.object  # Lấy thông tin của appointment từ đối tượng được trả về bởi DetailView

        # Lấy danh sách PrescriptionLines tương ứng với appointment
        prescription_lines = appointment.prescriptionlines_set.all()

        # Thêm danh sách PrescriptionLines vào context để hiển thị trong template
        context['prescription_lines'] = prescription_lines
        return context


