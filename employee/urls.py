# medicineapp/urls.py
from django.urls import path
from .views import AddEmployeeViews, UpdateemployeeViews, delete_EmployeeViews, displayEmployeeview

urlpatterns = [
    path('add_employee/', AddEmployeeViews.as_view(), name='add_employee'),
    path('display/',  displayEmployeeview, name='display'),
    path('desig/<slug:desig_slug>/', displayEmployeeview, name='desig_slug'),
    path('edit/<int:pk>/', UpdateemployeeViews.as_view(), name='edit_employee'),
    path('delete/<int:id>/', delete_EmployeeViews, name='delete_employee'),

]
