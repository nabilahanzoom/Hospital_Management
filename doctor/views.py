from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .forms import  ReviewForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, FormView
from django.urls import reverse_lazy


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# for email
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import DoctorRegistrationForm

# Create your views here.

# user can see all doctor
def doctorviews(request):
    data = models.DoctorModel.objects.all()
    
    return render(request, 'doctor.html', {'data':data})

# user can see all designationviews
def designationviews(request, designation_slug = None):
    data = models.DoctorModel.objects.all()
    if designation_slug is not None:
        designation = models.DesignationModel.objects.get(slug = designation_slug)
        data = models.DoctorModel.objects.filter(designation = designation)
        
    designation = models.DesignationModel.objects.all()
    return render(request, 'designation.html', {'data':data, 'designation': designation})

# user can see all  specializationviews
def specializationviews(request, specialization_slug = None):
    data = models.DoctorModel.objects.all()
    if specialization_slug is not None:
        specialization = models.SpecializationModel.objects.get(slug = specialization_slug)
        data = models.DoctorModel.objects.filter(specialization = specialization)
        
    specialization = models.SpecializationModel.objects.all()
    return render(request, 'specialization.html', {'data':data, 'specialization': specialization})



# User can see doctor details
class DoctorDetailsView(DetailView):
    model = models.DoctorModel
    # pk_url_kwarg = 'id'
    template_name = 'doctor_details.html'
    context_object_name = 'doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get reviews related to the current doctor
        reviews = ReviewModel.objects.filter(doctor=self.object)
        
        context['reviews'] = reviews
        return context


# i can delete it . it not need
class RegistrationView(View):
    template_name = 'doctor_regostration.html'
    form_class = DoctorRegistrationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            doctor = form.save(commit=False)  
            user = doctor.user 

            # Send confirmation email
            # email_subject = 'Confirm your email'
            # email_body = render_to_string('confirm_email.html')

            # email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            # email.attach_alternative(email_body, "text/html")
            # email.send()
            # doctor.save()
            # return HttpResponse("Check your email for confirmation.")
        
        return render(request, self.template_name, {'form': form})

from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

class UserRegistrationViews(FormView):
    template_name = 'user_regostration.html'
    form_class = DoctorRegistrationForm
    success_url =reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid functions call hobe jodi sob thik thake

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required  # You may adjust the login requirement as needed
def doctor_registration1(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            
            # Get or create DoctorModel instance for the user
            doctor_instance, created = DoctorModel.objects.get_or_create(user=user)

            # Update many-to-many fields using set() method
            doctor_instance.designation.set(form.cleaned_data['designation'])
            doctor_instance.specialization.set(form.cleaned_data['specialization'])
            doctor_instance.available_time.set(form.cleaned_data['available_time'])

            # Update other fields
            doctor_instance.image = form.cleaned_data['image']
            doctor_instance.fee = 1000
            doctor_instance.qualification = form.cleaned_data['qualification']
            doctor_instance.meet_link = form.cleaned_data['meet_link']
            print(doctor_instance.fee)
            # Save the DoctorModel instance
            doctor_instance.save()

            return redirect('home')  # Redirect to a success page or another view

    else:
        form = DoctorRegistrationForm()

    return render(request, 'doctor_regostration.html', {'form': form})



# class ActivateAccountView(View):
#     def get(self, request, uidb64, token):
#         try:
#             uid = force_str(urlsafe_base64_decode(uidb64))
#             user = get_user_model().objects.get(pk=uid)

#             if user and default_token_generator.check_token(user, token):
#                 user.is_active = True
#                 user.save()
#                 return HttpResponse("Your account is now activated. You can log in.")
#             else:
#                 return HttpResponse("Activation link is invalid.")
#         except Exception as e:
#             return HttpResponse("Activation link is invalid.")



# review views

@login_required
def review_view(request, doctor_id):
    dr = get_object_or_404(models.DoctorModel, pk=doctor_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user.patientmodel
            review.doctor = dr
            review.save()
            return redirect('doctor')  
    else:
        form = ReviewForm()

    return render(request, 'review.html', {'form': form, 'dr': dr})

from .models import DoctorModel, ReviewModel
@login_required
def doctor_reviews_view(request, doctor_id):
    doctor = get_object_or_404(DoctorModel, pk=doctor_id)
    reviews = ReviewModel.objects.filter(doctor=doctor)

    return render(request, 'display_review.html', {'doctor': doctor, 'reviews': reviews})
