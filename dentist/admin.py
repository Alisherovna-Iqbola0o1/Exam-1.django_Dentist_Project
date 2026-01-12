from django.contrib import admin
from .models import Clinic, Dentist, WorkingHours

# Register your models here.

admin.site.register(Clinic)
admin.site.register(Dentist)
admin.site.register(WorkingHours)
