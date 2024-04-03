from shop.models import Client
from django.http import HttpResponse


def get_clients(request):
    clients = Client.objects.all()
    res = '<br>'.join([str(client) for client in clients])
    return HttpResponse(res)


def get_client(request, pk):
    client = Client.objects.filter(pk=pk).first()
    return HttpResponse(client)


def delete_client(request, pk):
    Client.objects.filter(pk=pk).delete()
    return HttpResponse('Client Deleted!')
