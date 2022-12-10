from django.shortcuts import render, redirect
from .models import *
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from gestionPedidos.models import Component
from decouple import config
import stripe

stripe.api_key = config("STRIPE_SECRET_KEY")

# Create your views here.

from django import forms

login_required
def showCart(request):

    cart = Cart.objects.filter(user=request.user)
    
    if not cart.exists():
        cart = Cart(user=request.user)
        cart.save()
        componentsInCart = ComponentsInCart.objects.filter(cart=cart)
        bikesInCart = BikesInCart.objects.filter(cart=cart)
    else:
        componentsInCart = ComponentsInCart.objects.filter(cart=cart[0])
        bikesInCart = BikesInCart.objects.filter(cart=cart[0])

    totalPriceComponent = 0
    totalPriceBike = 0

    for componentInCart in componentsInCart:
        totalPriceComponent += componentInCart.component.precio

    for bikeInCart in bikesInCart:
        totalPriceBike += bikeInCart.bike.precio


    print(totalPriceComponent)
    print(totalPriceBike)
    total = totalPriceComponent + totalPriceBike
    

    return render(request, 'pages/cart.html', {'componentsInCart': componentsInCart, 'bikesInCart': bikesInCart, 'precioTotal': total})


def buy(request):
    cart = Cart.objects.filter(user=request.user)
    
    if not cart.exists():
        cart = Cart(user=request.user)
        cart.save()
        componentsInCart = ComponentsInCart.objects.filter(cart=cart)
        bikesInCart = BikesInCart.objects.filter(cart=cart)
    else:
        componentsInCart = ComponentsInCart.objects.filter(cart=cart[0])
        bikesInCart = BikesInCart.objects.filter(cart=cart[0])

    totalPriceComponent = 0
    totalPriceBike = 0

    for componentInCart in componentsInCart:
        totalPriceComponent += componentInCart.component.precio

    for bikeInCart in bikesInCart:
        totalPriceBike += bikeInCart.bike.precio
    total = totalPriceComponent + totalPriceBike



    return render(request, 'pages/buy.html', {'componentsInCart': componentsInCart, 'bikesInCart': bikesInCart, 'precioTotal': total});

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

@login_required
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
            bici.precio = cuadro.precio + manillar.precio + sillin.precio + rueda.precio + camara.precio
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

            cart = Cart.objects.filter(user=request.user)
            if not cart.exists():
                cart = Cart(user=request.user)
                cart.save()
                bikeInCart = BikesInCart(cart=cart, bike=bici)
            else:
                bikeInCart = BikesInCart(cart=cart[0], bike=bici)

            bikeInCart.save()

            return redirect("/cart/")

        else:
            msg = 'Form is not valid'

    return render(request, "pages/configureBike.html", diccionario)

@login_required
def editBike(request, bike_id):
    msg = None

    cuadros = Component.objects.filter(type_component="CB")
    manillares = Component.objects.filter(type_component="MN")
    sillines = Component.objects.filter(type_component="SL")
    ruedas = Component.objects.filter(type_component="RD")
    camaras = Component.objects.filter(type_component="CR")

    diccionario = {
        "bike_id": bike_id,
        "edit_mode": True,
        "msg": msg,
        "cuadros": cuadros,
        "manillares": manillares,
        "sillines": sillines,
        "ruedas": ruedas,
        "camaras": camaras
    }

    if request.method == "GET":
        bike = Bike.objects.filter(id=bike_id)
        if not bike.exists():
            return redirect("/configureBike/")
        
        diccionario.update({"name": bike[0].name})

        oldComponents = ComponentBike.objects.filter(bike=bike[0])
        for oldComponent in oldComponents:
            if oldComponent.component.type_component == "SL":
                diccionario.update({"sillin": oldComponent.component.id})
            elif oldComponent.component.type_component == "RD":
                diccionario.update({"rueda": oldComponent.component.id})
            elif oldComponent.component.type_component == "MN":
                diccionario.update({"manillar": oldComponent.component.id})
            elif oldComponent.component.type_component == "CR":
                diccionario.update({"camara": oldComponent.component.id})
            elif oldComponent.component.type_component == "CB":
                diccionario.update({"cuadro": oldComponent.component.id})
            
    if request.method == "POST":
        form = forms.Form(request.POST)
        if form.is_valid():
            nombre = request.POST['nombre']
            cuadro = Component.objects.get(pk=request.POST['cuadro'])
            manillar = Component.objects.get(pk=request.POST['manillar'])
            sillin = Component.objects.get(pk=request.POST['sillin'])
            rueda = Component.objects.get(pk=request.POST['rueda'])
            camara = Component.objects.get(pk=request.POST['camara'])

            bike = Bike.objects.filter(id=bike_id)[0]
            bike.name = nombre
            bike.precio = cuadro.precio + manillar.precio + sillin.precio + rueda.precio + camara.precio
            bike.save()

            newComponents = [cuadro, manillar, sillin, rueda, camara]
            oldComponents = ComponentBike.objects.filter(bike=bike)
            for i in range(0,5):
                componentToSave = oldComponents[i]
                componentToSave.component = newComponents[i]
                componentToSave.save()

            return redirect("/cart/")

        else:
            msg = 'Form is not valid'

    return render(request, "pages/configureBike.html", diccionario)

def checkout(request):
    token = request.POST['stripeToken']

    try:
        charge = stripe.Charge.create(
            amount=1000,
            currency='EUR',
            description='Example charge',
            source=token,
        )
    except stripe.error.CardError as e:
        # Since it's a decline, stripe.error.CardError will be caught
        body = e.json_body
        err = body.get('error', {})
        print("Status is: %s" % e.http_status)
        print("Type is: %s" % err.get('type'))
        print("Code is: %s" % err.get('code'))
        # param is '' in this case
        print("Param is: %s" % err.get('param'))
        print("Message is: %s" % err.get('message'))
        return HttpResponse(status=e.http_status)
    except stripe.error.RateLimitError as e:
        # Too many requests made to the API too quickly
        return HttpResponse(status=e.http_status)
    except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe's API
        return HttpResponse(status=e.http_status)
    except stripe.error.AuthenticationError as e:
        # Authentication with Stripe's API failed
        # (maybe you changed API keys recently)
        return HttpResponse(status=e.http_status)
    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        return HttpResponse(status=e.http_status)
    except stripe.error.StripeError as e:
        # Display a very generic error
        return HttpResponse(status=e.http_status)

@login_required
def inventory(request):
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
        form = InventoryForm(request.POST)
        if form.is_valid():
            cart = Cart.objects.filter(user=request.user)
            if not cart.exists():
                cart = Cart(user=request.user)
                cart.save()
            
            for componentForm in form.cleaned_data['componentes']:
                componentInCart = ComponentsInCart(cart=cart[0], component=componentForm)
                componentInCart.save()

            return redirect("/cart/")
    return render(request, "pages/inventory.html", diccionario)

def deleteBike(request, bike_id):
    for tabla in ComponentBike.objects.filter(bike = Bike.objects.get(id=bike_id)):
        tabla.delete()
    BikesInCart.objects.get(bike = Bike.objects.get(id=bike_id)).delete()
    Bike.objects.get(id=bike_id).delete()
    return redirect("/cart/")
        