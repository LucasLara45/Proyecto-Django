from django.urls import path
from .views import ServiceList, ServiceCreate

urlpatterns = [
    path('services/', ServiceList.as_view(), name='service_list'),
    path('services/<str:category>/', ServiceList.as_view(), name='service_list_category'),
    path('create/', ServiceCreate.as_view(), name='service_create'),
]