from django.urls import path

from webapp.views.products import add_product_view
from webapp.views.products import add_category_view
from webapp.views.base import index_view
from webapp.views.products import product_view
from webapp.views.products import category_view
from webapp.views.products import delete_view


urlpatterns = [
    path('', index_view, name='index'),
    path('products', index_view, name='index'),
    path('product_list/add/', add_product_view, name='product_add'),
    path('category_list/add/', add_category_view, name='category_add'),
    path('product_list/', index_view),
    path('product_list/<int:pk>', product_view, name='product_detail'),
    path('category_list/<int:pk>', category_view, name='category_detail'),
    path('delete_product/<int:pk>', delete_view, name='delete')
]
