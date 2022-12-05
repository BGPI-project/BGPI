from django.shortcuts import render
from .models import *
<<<<<<< HEAD
from django.db.models import Q
=======
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
>>>>>>> migromdor
# Create your views here.


def showCart(request):

    cart = Cart.objects.all()
    component = Component.objects.all()
    ls = [1,2,3,4,5]

    

<<<<<<< HEAD
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


     
=======
    return render(request, 'pages/cart.html', {'cart': cart, 'component': component, 'ls':ls})
@login_required
def index(request):
    usuario=request.user

    return render(request, 'pages/index.html',{'usuario':usuario})

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('pages/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('pages/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('pages/page-500.html')
        return HttpResponse(html_template.render(context, request))
>>>>>>> migromdor
