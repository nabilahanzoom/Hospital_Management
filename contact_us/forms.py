from django import forms

# from .models import AppiontmentModel

# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = AppiontmentModel
#         fields = ['appointment_type', 'symptop', 'time']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    sub = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea)