from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.views import LoginView

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
        