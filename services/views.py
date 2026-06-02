from unicodedata import category

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView , UpdateView , DeleteView
from services.models import Service, ServiceOrder
from services.forms import ServiceForm, ServiceOrderForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from urllib.parse import quote
from django.contrib.auth.mixins import LoginRequiredMixin


class ServiceList(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'

    def get_queryset(self):
        category = self.kwargs.get('category')

        if category:
            return Service.objects.filter(category=category)

        return Service.objects.all()

    def get_template_names(self):
        category = self.kwargs.get('category')
        if category == 'reacondicionado':
            return ['services/reaconditioned_list.html']
        return ['services/service_list.html']

class ServiceCreate(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('service_list')

class ServiceUpdate(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_form.html'
    success_url = reverse_lazy('service_list')

class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy('service_list')
    
class ServiceOrderCreate(LoginRequiredMixin, CreateView):
    model = ServiceOrder
    form_class = ServiceOrderForm
    template_name = 'services/order_form.html'
    success_url = reverse_lazy('service_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.service_id = self.kwargs['service_id']

        order = form.save()

        message = f"""
        Hola, quiero solicitar un servicio.
        Servicio: {order.service.title}
        Nombre: {order.full_name}
        Teléfono: {order.phone}
        Dirección: {order.address}
        Método de pago: {order.payment_method}
        Detalles:
        {order.notes}
        """
        encoded_message = quote(message)
        whatsapp_url = f"https://wa.me/5491126400798?text={encoded_message}"
        return redirect(whatsapp_url)
        
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['service'] = get_object_or_404(Service,id=self.kwargs['service_id'])
        return context

class MyOrdersView(LoginRequiredMixin, ListView):
    model = ServiceOrder
    template_name = "services/my_orders.html"

    def get_queryset(self):
        return ServiceOrder.objects.filter(
            user=self.request.user
        ).order_by("-created_at")