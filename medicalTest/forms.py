from django import forms
from .models import MedicalTestModel

class AddmedicalTestForm(forms.ModelForm):
    class Meta:
        model = MedicalTestModel
        fields = '__all__'
        
class EditmedicalTestForm(forms.ModelForm):
    class Meta:
        model = MedicalTestModel
        fields = '__all__'