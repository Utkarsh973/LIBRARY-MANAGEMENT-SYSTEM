import json
from django.conf import settings
from django.core.management.base import BaseCommand
from items_app.models import Item

class Command(BaseCommand):
    help = 'create files from JSON file'
    
    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR/ 'data' / 'books.json'
        assert datafile.exists()
        
        with open(datafile, 'r') as f :
            data = json.load(f)
        
        books = [Item(**book) for book in data]
        Item.objects.bulk_create(books)
        