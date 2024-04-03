from django.core.management.base import BaseCommand
from shop.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(
            name='John', email='john@example.com', phone_number=123456789,
            address='Moscow')
        client.save()
        self.stdout.write(f'{client}')
