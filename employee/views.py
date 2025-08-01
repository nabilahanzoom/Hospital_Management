from django.shortcuts import render, redirect
from .forms import AddEmployeeForm
from .models import DesignationModel, EmployeeModel
from django.views.generic import ListView, UpdateView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

# Create your views here.
class AddEmployeeViews(CreateView):
    model = EmployeeModel
    form_class = AddEmployeeForm
    template_name = 'employee.html'
    success_url = reverse_lazy('display')

class UpdateemployeeViews(UpdateView):
    model = EmployeeModel
    form_class = AddEmployeeForm
    template_name = 'employee.html'
    success_url = reverse_lazy('display') 

@user_passes_test(lambda u: u.is_superuser)
def delete_EmployeeViews(request, id):
    record = EmployeeModel.objects.get(pk=id)
    record.delete()
    return redirect('display')

@login_required
def displayEmployeeview(request, desig_slug = None):
    data = EmployeeModel.objects.all()
    if desig_slug is not None:
        designation = DesignationModel.objects.get(slug = desig_slug)
        data = EmployeeModel.objects.filter(designation = designation)
        
    designation = DesignationModel.objects.all()
    return render(request, 'Displayemployee.html', {'data':data, 'designation': designation})


