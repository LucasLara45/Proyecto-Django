from django.urls import path
from .views import MyOrdersView, ServiceDelete, ServiceList, ServiceCreate, ServiceOrderCreate, ServiceUpdate, ServiceDelete

urlpatterns = [
    path('', ServiceList.as_view(), name='service_list'),
    path('services/<str:category>/', ServiceList.as_view(), name='service_list_category'),
    path('create/', ServiceCreate.as_view(), name='service_create'),
    path('edit/<int:pk>/', ServiceUpdate.as_view(), name='service_update'),
    path('delete/<int:pk>/', ServiceDelete.as_view(), name='service_delete'),
    path('order/<int:service_id>/', ServiceOrderCreate.as_view(), name='service_order_create'),
    path("mis-pedidos/",MyOrdersView.as_view(),name="my_orders"),
]