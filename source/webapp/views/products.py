from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Products
from webapp.models import Categories


def get_category(request):
    categories = Categories.objects.filter(category=f"{request.POST.get('categories')}")
    for category in categories:
        return Categories.objects.get(pk=category.id)


def add_product_view(request):
    if request.method == "GET":
        category = Categories.objects.values('category')
        return render(request, "product_create.html", context={
            'category': category
        })
    product_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'category': get_category(request),
        'price': request.POST.get('price'),
        'image': request.POST.get('image')
    }
    product = Products.objects.create(**product_data)
    return redirect('product_detail', pk=product.pk)


def add_category_view(request):
    if request.method == "GET":
        return render(request, "category_create.html")
    category_data = {
        'category': request.POST.get('category'),
        'description': request.POST.get('description')
    }
    category = Categories.objects.create(**category_data)
    return redirect('category_detail', pk=category.pk)


def product_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'product.html', context={'product': product})


def category_view(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    return render(request, 'category.html', context={'category': category})


def delete_view(request, pk):
    task = get_object_or_404(Products, pk=pk)
    task.delete()
    return redirect('/')
