from django.shortcuts import render, redirect, get_object_or_404
from .forms import AppointmentForm, prescriptionForm
from doctor.models import DoctorModel
from patient.models import PatientModel
from .models import AppiontmentModel, prescriptionModel
from django.views import View
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# create a new appointment
def create_appointment(request, id):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            patient, created = PatientModel.objects.get_or_create(user=request.user)

            doctor =  DoctorModel.objects.get(pk=id)

            # Create appointment
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.doctor = doctor
            appointment.save()
            return redirect('profile')  
    else:
        form = AppointmentForm()

    return render(request, 'create_appointment.html', {'form': form})


# Admin can see all appointment for all doctor
class DoctorAppointmentsView(View):
    template_name = 'doctor_appointments.html'

    def get(self, request, doctor_id):
        doctor = get_object_or_404(DoctorModel, id=doctor_id)
        appointments = AppiontmentModel.objects.filter(doctor=doctor)
        return render(request, self.template_name, {'doctor': doctor, 'appointments': appointments})

#  admin change Appointment status pending to running and running to pending
def ChangeAppointmentStatusView(request, appointment_id):
    appointment = get_object_or_404(AppiontmentModel, id=appointment_id)

    if appointment.appointment_status == 'Pending':
        if appointment.appointment_type == "Online":
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('admin_email.html', {'user' : appointment.patient.user, 'doctor' : appointment.doctor})
            
            email = EmailMultiAlternatives(email_subject , '', to=[appointment.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

        appointment.appointment_status = 'Running'
        appointment.save()

    elif appointment.appointment_status == 'Running':
        appointment.appointment_status = 'Pending'
        appointment.save()
       
    return redirect('doctor_appointments', doctor_id=appointment.doctor.id)


# Doctor change Appointment status running to complate
def DoctoChangeAppointmentStatusView(request, appointment_id):
    appointment = get_object_or_404(AppiontmentModel, id=appointment_id)
    if appointment.appointment_status == 'Running':
        appointment.appointment_status = 'Completed'
        appointment.save()
       
    return redirect('doctor_profile')

# Admin can delete appointment record
def delete_appointment(request, appointment_id):
    appointment_instance = get_object_or_404(AppiontmentModel, id=appointment_id)
    appointment_instance.delete()
    return redirect('doctor_appointments', doctor_id=appointment_instance.doctor.id)


# make prections 

def create_prescription(request, patient_id):
    
    patient = PatientModel.objects.get(pk=patient_id)
    doctor = DoctorModel.objects.get(user=request.user)

    if request.method == 'POST':
        form = prescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.patient = patient
            prescription.doctor = doctor
            prescription.save()
            return redirect('doctor_profile')
    else:
        form = prescriptionForm()

    return render(request, 'create_prescription.html', {'form': form, 'patient': patient, 'doctor': doctor})
