from django.urls import path
from shop.views import get_clients, get_client, delete_client, create_client

urlpatterns = [
    path('clients/', get_clients, name='clients'),
    path('clients/<int:pk>/', get_client, name='get_client'),
    path('clients/create/', create_client, name='create_client'),
    path('clients/delete/<int:pk>/', delete_client, name='delete')
]
