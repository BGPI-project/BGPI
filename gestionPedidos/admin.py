from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Bike)
admin.site.register(Component)
admin.site.register(ComponentBike)
admin.site.register(Cart)
admin.site.register(ComponentsInCart)
admin.site.register(BikesInCart)


