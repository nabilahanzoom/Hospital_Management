from django import forms
from .models import DoctorModel, ReviewModel, DesignationModel, SpecializationModel, AvailableTimeModel

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DoctorRegistrationForm(UserCreationForm):
    image = forms.ImageField(required=False)
    designation = forms.ModelMultipleChoiceField(queryset=DesignationModel.objects.all())
    specialization = forms.ModelMultipleChoiceField(queryset=SpecializationModel.objects.all())
    available_time = forms.ModelMultipleChoiceField(queryset=AvailableTimeModel.objects.all())
    fee = forms.IntegerField()
    qualification = forms.CharField(max_length=100, required=False)
    meet_link = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2','image','designation','specialization','available_time','fee','qualification','meet_link']

        
    def save(self, commit= True):
        user =  super().save(commit=False)
        if commit == True:
            user.save() # user model a data save hobe
            
            
        
            image = self.cleaned_data.get('image')

            designation = self.cleaned_data.get('designation')
            specialization = self.cleaned_data.get('specialization')
            
            available_time = self.cleaned_data.get('available_time')
            fee = self.cleaned_data.get('fee')
            qualification = self.cleaned_data.get('qualification')
            meet_link = self.cleaned_data.get('meet_link')
            
            # UserAddressModel model a data save hobe
            doctor_instance = DoctorModel.objects.create(
            user=user,
            image=image,
            fee=fee,
            qualification=qualification,
            meet_link=meet_link,
            )

            doctor_instance.designation.set(designation)
            doctor_instance.specialization.set(specialization)
            doctor_instance.available_time.set(available_time)
            
        return user
    
    










class ReviewForm(forms.ModelForm):
       
    class Meta:
        model = ReviewModel
        fields = ['body', 'ratting']
