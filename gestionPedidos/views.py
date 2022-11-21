from django.shortcuts import render
from .models import *
# Create your views here.


def showCart(request):

    cart = Cart.objects.all()
    component = Component.objects.all()
    ls = [1,2,3,4,5]

    

    return render(request, 'cart.html', {'cart': cart, 'component': component, 'ls':ls})