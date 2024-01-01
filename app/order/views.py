from django.shortcuts import render
from product.models import ProductItem
# Create your views here.

def basket(request):
    context = {
        'items' : ProductItem.objects.filter(user=request.user, status=0)
    }
    return render(request, 'order/basket.html', context)