from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.


def showCart(request):

    cart = Cart.objects.all()
    component = Component.objects.all()
    ls = [1,2,3,4,5]

    

    return render(request, 'cart.html', {'cart': cart, 'component': component, 'ls':ls})


def list_products(request):
    busqueda=request.POST.get("buscar")
    products= Component.objects.all()

    if busqueda:
        products=Component.objects.filter(
             Q(name__icontains = busqueda) | 
            Q(type_component__icontains = busqueda) 
        ).distinct()
    
    return render (request,'navigation.html',{'products':products})


     