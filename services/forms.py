from django import forms

from .models import ServiceOrder,Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

class ServiceOrderForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = ['full_name','phone','address','email','payment_method','notes',]