from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "core/index.html"

class ContactView(TemplateView):
    template_name = "core/contact.html"