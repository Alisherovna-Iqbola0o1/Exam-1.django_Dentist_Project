from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('clinic_list')), 
    path('', include('dentist.urls')),                
    path('clients/', include('clients.urls')),       
]
