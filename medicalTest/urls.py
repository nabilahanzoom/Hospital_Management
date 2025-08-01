# medicineapp/urls.py
from django.urls import path
from .views import AddMedicalTestViews, EditMedicalTestViews, delete_MedicalTestViews, displayMedicalTestview, applyfortestviews

urlpatterns = [
    path('create_test/', AddMedicalTestViews.as_view(), name='create_test'),
    path('seeTest/',  displayMedicalTestview, name='seeTset'),
    path('category/<slug:category_slug>/', displayMedicalTestview, name='category_slug'),
    path('edit/<int:pk>/', EditMedicalTestViews.as_view(), name='test_edit'),
    path('delete/<int:id>/', delete_MedicalTestViews, name='test_delete'),
    path('apply/<int:test_id>/', applyfortestviews, name='test_apply'),

]
