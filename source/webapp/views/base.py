from django.shortcuts import render
from webapp.models import Products


def index_view(request):
    products = Products.objects.all()
    context = {
        "products": products
    }
    return render(request, "index.html", context)

