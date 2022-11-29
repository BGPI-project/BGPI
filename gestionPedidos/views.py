from django.shortcuts import render
from .models import *
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from gestionPedidos.models import Component
# Create your views here.

from django import forms

def showCart(request):

    cart = Cart.objects.all()
    component = Component.objects.all()
    ls = [1,2,3,4,5]

    

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

def configureBike(request):
    msg = None

    cuadros = Component.objects.filter(type_component="CB")
    manillares = Component.objects.filter(type_component="MN")
    sillines = Component.objects.filter(type_component="SL")
    ruedas = Component.objects.filter(type_component="RD")
    camaras = Component.objects.filter(type_component="CR")

    diccionario = {
            "msg": msg,
            "cuadros": cuadros,
            "manillares": manillares,
            "sillines": sillines,
            "ruedas": ruedas,
            "camaras": camaras
        }

    if request.method == "POST":
        form = forms.Form(request.POST)
        if form.is_valid():
            nombre = request.POST['nombre']
            cuadro = Component.objects.get(pk=request.POST['cuadro'])
            manillar = Component.objects.get(pk=request.POST['manillar'])
            sillin = Component.objects.get(pk=request.POST['sillin'])
            rueda = Component.objects.get(pk=request.POST['rueda'])
            camara = Component.objects.get(pk=request.POST['camara'])

            bici = Bike(name=nombre)
            bici.save()

            component1 = ComponentBike(bike=bici, component=cuadro)
            component1.save()

            component2 = ComponentBike(bike=bici, component=manillar)
            component2.save()

            component3 = ComponentBike(bike=bici, component=sillin)
            component3.save()

            component4 = ComponentBike(bike=bici, component=rueda)
            component4.save()

            component5 = ComponentBike(bike=bici, component=camara)
            component5.save()

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'

    return render(request, "pages/configureBike.html", diccionario)