from django.shortcuts import render, redirect

from django.conf import settings 
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.views.generic.base import TemplateView
import stripe

# Create your views here.

@csrf_protect
@require_http_methods(["GET"])
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)