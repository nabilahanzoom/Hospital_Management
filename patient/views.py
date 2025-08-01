from django.shortcuts import render, redirect
from . import forms
from patient.models import PatientModel
from doctor.models import DoctorModel
from appointment.models import AppiontmentModel, prescriptionModel

from .forms import RegisterForm
from django.views.generic import FormView, DetailView, CreateView
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from .forms import LoginForm
from django.contrib import messages

# Create your views here.

# user/ patient can registration
class UserRegistrationViews(FormView):
    template_name = 'user_regostration.html'
    form_class = forms.RegisterForm
    success_url =reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# class Userloginviews(LoginView):
#     template_name = 'user_login.html'
    
#     def get_success_url(self):
#         return reverse_lazy('home')


# All type of user can logout 
class userlogoutview(View):
    def get(self, request):
        logout(request)
        messages.success(self.request, 'Logout Successfully. Welcome Back!')
        return redirect('home')


# patient profile page
def profileview(request):
    data = PatientModel.objects.filter(user=request.user)
   
    current_patient = request.user.patientmodel
    print(current_patient)
    apdata = AppiontmentModel.objects.filter(patient=current_patient)
    prescription = prescriptionModel.objects.filter(patient=current_patient)
    # for i in prescription:
    #     print(i.body)
    return render(request, 'profile.html', {'data':current_patient, 'appointment': apdata, 'prescription': prescription})


# custom login for user doctor and admin
class CustomLoginView(View):
    template_name = 'user_login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                # Check the user's role and redirect accordingly
                if hasattr(user, 'doctormodel'):
                    messages.success(self.request, 'Login Successfully. Welcome Back!')
                    return redirect('home')
                elif hasattr(user, 'patientmodel'):
                    messages.success(self.request, 'Login Successfully. Welcome Back!')
                    return redirect('home')
                elif user.is_superuser:
                    messages.success(self.request, 'Login Successfully. Welcome Back!')
                    return redirect('home')

        return render(request, self.template_name, {'form': form})

# Doctor profile page
class DoctorProfileView(View):
    template_name = 'doctor_profile.html'

    def get(self, request):
        doctor = DoctorModel.objects.get(user=request.user)
        appointments = AppiontmentModel.objects.filter(doctor=doctor)
        return render(request, self.template_name, {'doctor': doctor, 'appointments': appointments})




# show all prescription for a single patient
def patient_prescriptions(request, patient_id):
    patient_prescriptions = prescriptionModel.objects.filter(patient_id=patient_id)
    return render(request, 'prescription.html', {'data': patient_prescriptions})

# show single prescription for a single patient

class Single_prescriptions(DetailView):
    model = prescriptionModel
    # pk_url_kwarg = 'id'
    template_name = 'single_prescription.html'




# Html to pdf download

# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from appointment.models import prescriptionModel
from .process import html_to_pdf 
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        print(pk)
        data = get_object_or_404(prescriptionModel, id=pk)
        print('data',data)
        open('templates/temp.html', "w").write(render_to_string('pdf.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')




