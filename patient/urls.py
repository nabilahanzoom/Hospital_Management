from django.urls import path

from . import views

urlpatterns = [
    path('register/',  views.UserRegistrationViews.as_view(), name='register'),
    path('login/',  views.CustomLoginView.as_view(), name='login'),
    path('profile/',  views.profileview, name='profile'),
    path('doctor_profile/',  views.DoctorProfileView.as_view(), name='doctor_profile'),
    path('logout/',  views.userlogoutview.as_view(), name='logout'),

    path('prescription/<int:patient_id>/', views.patient_prescriptions, name='patient_prescription'),
    path('single_prescription/<int:pk>/', views.Single_prescriptions.as_view(), name='single_prescription'),


    path('pdf/<int:pk>/', views.GeneratePdf.as_view(), name="pdf"), 

    # path('', views.index, name='index'),
    # path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    # path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
]