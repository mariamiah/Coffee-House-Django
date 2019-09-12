from django.shortcuts import render, get_object_or_404
from .models import Store

# Create your views here.
# view all stores
def stores(request):
    stores = Store.objects.all()
    return render(request, 'storeapp/stores.html', {'stores': stores})

def detail(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    return render(request, 'storeapp/detail.html', {'store': store})
