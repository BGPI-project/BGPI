from django.shortcuts import render, redirect

from django.conf import settings 
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.views.generic.base import TemplateView
import stripe

from gestionPedidos.models import Order

# Create your views here.

@csrf_protect
@require_http_methods(["GET"])
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_protect
@require_http_methods(["GET"])
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/paymnets/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
    
    try:
        orders = Order.objects.filter(user=request.user)
        if orders.exists():
            order = orders[0]
        else:
            return redirect("/cart/")

        line_items=[]
        line_items.append({
            'price_data': {
            'currency': 'eur',
            'product_data': {
              'name': 'Ordered by ' + order.user.first_name,
            },
            'unit_amount': int(order.precio * 100),
          },
          'quantity': 1,
        })
      
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + 'cancelled/',
            payment_method_types=['card'],
            mode='payment',
            line_items=line_items,
        )
                
        return JsonResponse({'sessionId': checkout_session['id']})
    except Exception as e:
        return JsonResponse({'error': str(e)})

@require_http_methods(["GET"])
def success_view(request):

    template_name = 'success.html'

    orders = Order.objects.filter(user=request.user)
    if orders.exists():
        order = orders[0]
        order.delete()
    else:
        return redirect("/cart/buy/")

    return render(request , template_name)

@require_http_methods(["GET"])
def cancelled_view(request):

    template_name = 'cancelled.html'

    orders = Order.objects.filter(user=request.user)
    if orders.exists():
        order = orders[0]
        order.delete()
    else:
        return redirect("/cart/buy/")
    
    return render(request , template_name)