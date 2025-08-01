from django.db import models
from doctor.models import DoctorModel, AvailableTimeModel
from patient.models import PatientModel
# Create your models here.

APPOINTMENT_STATUS = [
    ('Pending', 'Pending'),
    ('Running', 'Running'),
    ('Completed', 'Completed'),
]

APPOINTMENT_TYPE = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]

class AppiontmentModel(models.Model):
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    appointment_status = models.CharField(max_length=30, choices=APPOINTMENT_STATUS, default='Pending')
    appointment_type = models.CharField(max_length=30, choices=APPOINTMENT_TYPE, default='Offline')
    symptop = models.TextField()
    cancel = models.BooleanField(default=False)


    def __str__(self):
        return f"DR. {self.doctor.user.first_name}, Patient:- {self.patient.user.first_name}"

class prescriptionModel(models.Model):
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"DR. {self.doctor.user.first_name}, Patient:- {self.patient.user.first_name}"