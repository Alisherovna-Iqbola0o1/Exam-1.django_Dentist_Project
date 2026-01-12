from django.urls import path
from . import views

urlpatterns = [
    path('clinics/', views.clinic_list, name='clinic_list'),
    path('dentists/', views.dentist_list, name='dentist_list'),
    path('working-hours/', views.working_hours, name='working_hours'),
]
