from django.shortcuts import render
from .models import Clinic, Dentist, WorkingHours

# Create your views here.

def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'dentist/clinic_list.html', {'clinics': clinics})


def dentist_list(request):
    dentists = Dentist.objects.all()
    return render(request, 'dentist/dentist_list.html', {'dentists': dentists})


def working_hours(request):
    hours = WorkingHours.objects.all()
    return render(request, 'dentist/working_hours.html', {'hours': hours})
