from django.urls import path
from .views import create_appointment, DoctorAppointmentsView, ChangeAppointmentStatusView, delete_appointment, DoctoChangeAppointmentStatusView, create_prescription

urlpatterns = [
    path('create_appointment/<int:id>/', create_appointment, name='create_appointment'),
    path('doctor_appointments/<int:doctor_id>/', DoctorAppointmentsView.as_view(), name='doctor_appointments'),
    path('change_status/<int:appointment_id>/', ChangeAppointmentStatusView, name='change_appointment_status'),
    path('Dr_change_status/<int:appointment_id>/', DoctoChangeAppointmentStatusView, name='Dr_change_appointment_status'),
    path('delete/<int:appointment_id>/', delete_appointment, name='delete_appointment'),
    path('prescription/<int:patient_id>/', create_prescription, name='create_prescription'),



   
]
