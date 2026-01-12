from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.location}"


class Dentist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinics = models.ManyToManyField(Clinic, related_name='dentists')
    working_days = models.CharField(max_length=100)
    working_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class WorkingHours(models.Model):
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()         # TimeField -> faqat soar va minut saqlidi, DateTimeField -> sana, soat, min(wartmas)

    def __str__(self):
        return f"{self.dentist} {self.day}, {self.start_time} - {self.end_time}"
