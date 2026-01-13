from django.shortcuts import render
from .models import Appointment
# Create your views here.

def appointment_list(request):
    return render(request, 'appointments/appointment_list.html', {
        'appointments': Appointment.objects.all()
    })
