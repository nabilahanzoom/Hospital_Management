
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServicesViews, name="service"),
    path('details/<int:pk>/', views.ServiceDetails.as_view(), name='service_details'),
    # path('generate-pdf/', views.render_to_pdf, name='generate_pdf'),


]

