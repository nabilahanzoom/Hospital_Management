from django import forms
from .models import MedicinelistModel

class MedicinelistForm(forms.ModelForm):
    class Meta:
        model = MedicinelistModel
        fields = '__all__'