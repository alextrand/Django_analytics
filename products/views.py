from django.shortcuts import render
from .models import Phone

# Create your views here.


def products(request):
    ctx = {}
    all_phones = Phone.objects.all()
    ctx['all_phones'] = all_phones
    return render(request, 'products/all_products.html', ctx)


def detail_view(request, pk):
    phone = Phone.objects.get(id=pk)
    ctx = {
        'phone_instance': phone
    }
    return render(request, 'products/detail_view.html', ctx)

