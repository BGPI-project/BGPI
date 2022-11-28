# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import *

urlpatterns = [

    # The home page
    path('cart/', showCart, name='Cart'),

    path('', index, name='index'),

]
