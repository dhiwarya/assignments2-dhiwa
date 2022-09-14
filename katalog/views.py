# TODO: Create your views here.
from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.

def show_catalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'list_item': data_catalog_item,
        'name': 'Dhiwa Arya Kusumah',
        'npm' : '2106657115',
    }
    return render(request, "katalog.html", context)