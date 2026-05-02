from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.views import LoginView

def index(request):
    # Verifica si el usuario ha dejado una reseña
    user_has_review = False 
    # Si el usuario está autenticado, verifica si ha dejado una reseña
    if request.user.is_authenticated: 
        user_has_review = Review.objects.filter(user=request.user).exists() 
    # Si el método de la solicitud es POST, intenta guardar la reseña
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            # Si el formulario es válido, intenta guardar la reseña. Si el usuario ya ha dejado una reseña, muestra un mensaje de error.
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
    # Si el método de la solicitud no es POST, muestra todas las reseñas y el formulario para dejar una nueva reseña (si el usuario no ha dejado una reseña).
    reviews = Review.objects.all().order_by('-id')
    form = ReviewForm()
    # Si el usuario ha dejado una reseña, no muestra el formulario para dejar una nueva reseña.
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
        