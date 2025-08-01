from django.shortcuts import render
from django.views.generic import DetailView
from . import models
# Create your views here.

def ServicesViews(request):
    data = models.ServiceModel.objects.all()
    return render(request, 'services.html', {'data':data})

class ServiceDetails(DetailView):
    model = models.ServiceModel
    # pk_url_kwarg = 'id'
    template_name = 'service_details.html'



