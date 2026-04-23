"""
URL configuration for refrig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
import os


urlpatterns = [
    path("", include("core.urls")),
    path('clients/', include('clients.urls')),
    path('services/', include('services.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # ¿Por qué necesitamos esto?
    # En DESARROLLO: Django NO sirve archivos estáticos automáticamente (razones de seguridad)
    # En PRODUCCIÓN: Un servidor web (Nginx, Apache) maneja los archivos estáticos
    # Esta sección SOLO se ejecuta cuando DEBUG=True, así se ve durante el desarrollo
    
    
    # Ruta completa a la carpeta donde están nuestros archivos estáticos
    static_root = os.path.join(settings.BASE_DIR, 'core', 'static')
    
    # Le decimos a Django: "Cuando pidan /static/..., busca en core/static/"
    # La función static() convierte rutas URL a rutas del servidor automáticamente
    # Ejemplo: /static/core/images/banner.jpg → busca en core/static/core/images/banner.jpg
    urlpatterns += static(settings.STATIC_URL, document_root=static_root)
    
    # Lo mismo para MEDIA (fotos subidas por usuarios)
    # Cuando pidan /media/..., busca en la carpeta media/
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)