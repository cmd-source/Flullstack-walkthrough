from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def all_products(request):

    products = Product.objects.all()

    query = None
    category = None

    if request.GET:
        if category in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__incategories)
            categories = products.objects.filter(category__name__incategories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
