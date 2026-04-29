from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

def index(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.save()
                return redirect('index')
            
    reviews = Review.objects.all().order_by('-id')
    form = ReviewForm()
    return render(request, 'core/index.html',{
        'reviews': reviews,
        'form': form
    })


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, "Credenciales inválidas.")
        return super().form_invalid(form)
        