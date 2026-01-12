from django.urls import path
from . import views

urlpatterns = [
    path('clients-list/', views.client_list, name='client_list'),
    path('orders/', views.order_list, name='order_list'),
]
