from django.shortcuts import render, redirect, get_object_or_404
from .forms import MedicinelistForm
from .models import MedicinelistModel, BuyMedicineModel
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

def create_medicine(request):
    if request.method == 'POST':
        form = MedicinelistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')  
    else:
        form = MedicinelistForm()

    return render(request, 'add_medicine.html', {'form': form})

class MedicineListView(ListView):
    model = MedicinelistModel
    template_name = 'medicine_list.html'  
    context_object_name = 'medicines'




class MedicineUpdateView(UpdateView):
    model = MedicinelistModel
    template_name = 'add_medicine.html'  
    fields = ['name', 'category', 'company', 'strength', 'price']

    def get_success_url(self):
        return reverse_lazy('medicine_list')  



@user_passes_test(lambda u: u.is_superuser)
def MedicineDeleteView(request, id):
    record = MedicinelistModel.objects.get(pk=id)
    record.delete()
    return redirect('medicine_list')


@login_required
def order_medicineviews(request):
    applicant = request.user.patientmodel
    BuyMedicineModel.objects.create(patient=applicant, tution=tution)
    return redirect('medicine_list')

from django.contrib import messages

@login_required
def Buy_medicineviews(request):
    messages.success(request, 'Medicine Buy Successfully. Welcome Back!')
    return redirect('medicine_list')


