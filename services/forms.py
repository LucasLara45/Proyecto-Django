from django import forms

from .models import ServiceOrder,Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = "__all__"

# class ServiceOrderForm(forms.ModelForm):
#     class Meta:
#         model = ServiceOrder
#         fields = ['client', 'service_type', 'description', 'price', 'photo']
#         widgets = {
#             'description': forms.Textarea(attrs={
#                 'rows': 4,
#                 'cols': 40,
#                 'class': 'form-control'
#             }),
#             'price': forms.NumberInput(attrs={
#                 'class': 'form-control',
#                 'step': '0.01'
#             }),
#             'client': forms.Select(attrs={
#                 'class': 'form-control'
#             }),
#             'service_type': forms.Select(attrs={
#                 'class': 'form-control'
#             }),
#         }