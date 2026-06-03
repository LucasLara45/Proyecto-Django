from django import forms
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre")
    email = forms.EmailField(label="Correo electrónico")
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'class': 'form-control'
            })
        }

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label="Nombre Real Completo")

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')