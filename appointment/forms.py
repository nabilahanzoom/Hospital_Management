from django import forms

from .models import AppiontmentModel, prescriptionModel

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppiontmentModel
        fields = ['appointment_type', 'symptop']

class prescriptionForm(forms.ModelForm):
    class Meta:
        model = prescriptionModel
        fields = ['body']