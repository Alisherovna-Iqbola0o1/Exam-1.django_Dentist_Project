from django.shortcuts import render
from .models import Client, Order

# Create your views here.

def client_list(request):
    clients = Client.objects.all()
    
def order_list(request):
    orders = Order.objects.all()
    
