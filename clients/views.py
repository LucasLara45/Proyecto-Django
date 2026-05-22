from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.db import IntegrityError
from .models import Review
from .forms import ReviewForm, ContactForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail

def index(request):
    user_has_review = False 
    if request.user.is_authenticated: 
        user_has_review = Review.objects.filter(user=request.user).exists() 
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                try:
                    review = form.save(commit=False)
                    review.user = request.user
                    review.save()
                
                except IntegrityError:
                    return render(request, 'core/index.html', {
                        'reviews': Review.objects.all(),
                        'form': form,
                        'error': 'UPS... Ya has dejado una reseña.',
                        'user_has_review': True
                    })
                return redirect('index')
    reviews = Review.objects.all().order_by('-id')
    form = ReviewForm()
    return render(request, 'core/index.html', {
        'reviews': reviews,
        'form': form,
        'user_has_review': user_has_review
    })


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def form_invalid(self, form):
        messages.error(self.request, "Credenciales inválidas.")
        return super().form_invalid(form)
        
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request , 'core/contact.html', {'form': form})

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class ReviewDelete(DeleteView):
    model = Review
    template_name = 'core/review_confirm_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user.is_authenticated
    
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            
            full_mensaje = f"""
            Nombre: {name}
            Email: {email}
            Mensaje: {mensaje}
            """

            send_mail(
                subject="Nuevo mensaje de contacto",
                message=full_mensaje,
                from_email=None,
                recipient_list=['lucaslara3000@gmail.com']
            )
            return redirect('index')
    return render(request , 'core/contact.html', {'form': form,})
    