# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # The home page
    path('cart/', showCart, name='Cart'),
    path('configureBike/', configureBike, name='ConfigureBike'),
    path('configureBike/<int:bike_id>/', editBike, name='editBike'),
    path('checkout/', checkout, name='checkout'),
    path('cart/buy', buy, name='buy'),

    path('', index, name='index'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
