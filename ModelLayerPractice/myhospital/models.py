from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.core.validators import MinValueValidator

class Patient(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    age = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name='Age'
    )
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male', verbose_name='Gender')
    note = models.TextField(verbose_name='Description', max_length=255)
    ethnicity = models.CharField(verbose_name='Ethnicity', max_length=100)
    blood_type_choice = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_type = models.CharField(max_length=10, choices=blood_type_choice, verbose_name='Blood_type')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Doctor(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name='Age'
    )
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male', verbose_name='Gender')
    MAJOR_CHOICES = [
        ('general_practitioner', 'General Practitioner'),
        ('internal_medicine', 'Internal Medicine'),
        ('surgery', 'Surgery'),
        ('obstetrics_and_gynecology', 'Obstetrics and Gynecology'),
        ('pediatrics', 'Pediatrics'),
        ('oral_and_maxillofacial_surgery', 'Oral and Maxillofacial Surgery'),
        ('others', 'Others')
    ]
    major = models.CharField(max_length=50, choices=MAJOR_CHOICES, verbose_name='Major')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    note = models.TextField(verbose_name='Description', max_length=255)
    service_price = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name='Service Price'
    )
    date_appointment = models.DateField()
    date_checkup = models.DateField()
    def __str__(self):
        return f"{self.name} - {self.patient}"

    def medicine_price(self):
        prescription_lines = self.prescriptionlines_set.all()  # Lấy tất cả PrescriptionLines của Appointment này
        total_medicine_price = sum(line.prescription_price for line in prescription_lines)
        return total_medicine_price

    def total_price(self):
        return self.service_price + self.medicine_price()

class PrescriptionLines(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
        default= 0,
        verbose_name='Quantity'
    )
    unit_price = models.FloatField(
        validators=[MinValueValidator(0)],
        default= 0,
        verbose_name='Price per unit'
    )

    @property
    def prescription_price(self):
        return self.unit_price * self.quantity

class MyUser(AbstractUser):
    pass