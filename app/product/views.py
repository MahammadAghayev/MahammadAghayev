from django.shortcuts import render

# Create your views here.

def product_list(request):
    products = Product.object.all()
    context = {
        'products': products
    }
    return render(request, 'product/list.html', context)