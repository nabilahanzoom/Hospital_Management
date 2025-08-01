# django builtin model forom
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import PatientModel

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

class RegisterForm(UserCreationForm):
    
    # If i want to any fields custom modify
    mobile_no = forms.IntegerField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=GENDER)
    
    class Meta:
        model = User
        
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile_no', 'age', 'gender']
        
    def save(self, commit= True):
        user =  super().save(commit=False)
        if commit == True:
            user.save() # user model a data save hobe
             
            # print(self.cleaned_data['mobile_no'])
            # PatientModel model a data save hobe
            PatientModel.objects.create(
                user = user,
                mobile_no = self.cleaned_data['mobile_no'],
                age = self.cleaned_data['age'],
                gender = self.cleaned_data['gender'],
                
            )
            
        return user
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)