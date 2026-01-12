from django.db import models
from django.conf import settings
from dentist.models import Dentist, Clinic

# Create your models here.

User = settings.AUTH_USER_MODEL  

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visit_count = models.IntegerField(default=0)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.client} - {self.dentist} at {self.appointment_time}"
