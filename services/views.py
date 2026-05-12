from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from services.models import Service
from services.forms import ServiceForm

class ServiceList(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'

    def get_queryset(self):

        category = self.kwargs.get('category')

        if category:
            return Service.objects.filter(category=category)

        return Service.objects.all()

class ServiceCreate(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_create.html'
    success_url = reverse_lazy('service_list')
    

