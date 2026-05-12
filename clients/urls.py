from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import index, MyLoginView

urlpatterns = [
    path('', index, name='index'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contact/', views.contact, name='contact'),
]