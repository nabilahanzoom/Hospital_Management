from django.shortcuts import render, redirect
from .forms import AddmedicalTestForm, EditmedicalTestForm
from .models import MedicalTestModel, CategoryModel, PatientTestModel
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

# Create your views here.
class AddMedicalTestViews(CreateView):
    model = MedicalTestModel
    form_class = AddmedicalTestForm
    template_name = 'add_medicalTest.html'

    success_url = reverse_lazy('seeTset')

class EditMedicalTestViews(UpdateView):
    model = MedicalTestModel
    form_class = AddmedicalTestForm
    template_name = 'add_medicalTest.html'
    success_url = reverse_lazy('seeTset') 

@user_passes_test(lambda u: u.is_superuser)
def delete_MedicalTestViews(request, id):
    record = MedicalTestModel.objects.get(pk=id)
    record.delete()
    return redirect('seeTset')

@login_required
def displayMedicalTestview(request, category_slug = None):
    data = MedicalTestModel.objects.all()
    if category_slug is not None:
        category = CategoryModel.objects.get(slug = category_slug)
        data = MedicalTestModel.objects.filter(Type = category)
        
    category = CategoryModel.objects.all()
    return render(request, 'display_test.html', {'data':data, 'category': category})


from django.contrib import messages
def applyfortestviews(request, test_id):
    applicant = request.user.patientmodel
    print(applicant)
    test = MedicalTestModel.objects.get(pk=test_id)

    PatientTestModel.objects.create(patient=applicant, test=test, test_status="Pending")
    messages.success(request, 'Successfully Apply for Medical test. Welcome Back!')
    return redirect('seeTset')