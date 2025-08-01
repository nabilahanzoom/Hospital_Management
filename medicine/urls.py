# medicineapp/urls.py
from django.urls import path
from .views import create_medicine, MedicineListView, MedicineUpdateView, MedicineDeleteView, order_medicineviews, Buy_medicineviews

urlpatterns = [
    path('create_medicine/', create_medicine, name='create_medicine'),
    path('medicines/', MedicineListView.as_view(), name='medicine_list'),
    path('edit/<int:pk>/', MedicineUpdateView.as_view(), name='medicine_edit'),
    path('delete/<int:id>/', MedicineDeleteView, name='medicine_delete'),
    path('order/<int:medicine_id>/', order_medicineviews, name='order_medicine'),
    path('buy/', Buy_medicineviews, name='buy_medicine'),



]
