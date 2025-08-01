from django.urls import path

from . import views

urlpatterns = [
    path('', views.contactViews, name='contact'),
  
]