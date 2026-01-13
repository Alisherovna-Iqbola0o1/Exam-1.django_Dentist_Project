from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dentist.urls')),
    path('', include('clients.urls')),
    path('', include('appointments.urls')),
]
