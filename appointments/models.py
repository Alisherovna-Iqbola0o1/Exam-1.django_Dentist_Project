from django.db import models
from django.conf import settings
from dentist.models import Dentist, Clinic
from clients.models import Client

User = settings.AUTH_USER_MODEL
# Create your models here.

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client} - {self.dentist} - {self.appointment_time}"