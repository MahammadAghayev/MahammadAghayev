from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Product, Category, Comment
# Create your views here.
from .forms import CommentForm, ProductItemForm
from django.urls import reverse




class ProductListView(generic.ListView):
    template_name = 'product/list.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 9


def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    context = {
        'products' : products
    }
    return render(request, 'product/list.html', context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    other_products = Product.objects.filter(category=product.category).exclude(
        id=product.slug
    ).distinct()

    reviews = Comment.objects.filter(product=product).order_by('-created_at')
    review_count = reviews.count()
    # product_item_form = ProductItemForm(request.POST or None, product_id=product.id)

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.product = product
            form.save()
            return redirect(reverse("product-detail", args=(product.slug,)))

    context = {
        'product' : product,
        'other_products' : other_products,
        'form': form,
        'reviews': reviews,
        'review_count': review_count,
    }
    return render(request, 'product/list.html', context)