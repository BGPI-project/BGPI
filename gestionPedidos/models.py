

from django.db import models
from django import forms

from enum import Enum
from django.contrib.auth.models import User
# Create your models here.

class Component(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(max_length=200, null=True)


    ND='No definido'
    SL='SL'
    RD='RD'
    MN='MN'
    CR='CR'
    CB='CB'

    TYPE= (
        (ND,'No definido'),
        (SL,'SL'),
        (RD,'RD'),
        (MN,'MN'),
        (CR,'CR'),
        (CB,'CB'),
        )

    type_component = models.CharField(
            max_length=255,
            choices=TYPE,
            default=ND) 

    def __str__(self):
        return self.name

class Bike(models.Model):
    name=models.CharField(max_length=30)
    precio=models.DecimalField(max_digits=7, decimal_places=2, default=0)
    image = models.CharField(max_length=200, null=True)

    

    def __str__(self):
        return self.name



class ComponentBike(models.Model):
    bike=models.ForeignKey(Bike,on_delete=models.CASCADE, blank=True, null=True)
    component=models.ForeignKey(Component,on_delete=models.CASCADE,blank=True, null=True)


    def __str__(self):
        return self.component.name



class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

class Order(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0)




class ComponentsInCart(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    component=models.ForeignKey(Component,on_delete=models.CASCADE)





class BikesInCart(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    bike=models.ForeignKey(Bike,on_delete=models.CASCADE)

class InventoryForm(forms.Form):
    componentes = forms.ModelMultipleChoiceField(
        queryset = Component.objects.all(), # not optional, use .all() if unsure
        widget  = forms.CheckboxSelectMultiple,
    )