from django.shortcuts import render
from dentist.models import Clinic, Dentist, WorkingHours

def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'clinic_list.html', {'clinics': clinics})

def dentist_list(request):
    dentists = Dentist.objects.all()
    return render(request, 'dentist_list.html', {'dentists': dentists})

def working_hours(request):
    hours = WorkingHours.objects.all()
    return render(request, 'working_hours.html', {'hours': hours})
