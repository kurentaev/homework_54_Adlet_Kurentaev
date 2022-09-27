from django.contrib import admin

from webapp.models import Products
from webapp.models import Categories


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'category', 'created_at', 'price', 'image']
    list_filter = ['id', 'title', 'description', 'category', 'created_at', 'price', 'image']
    search_fields = ['title', 'category']
    fields = ['id', 'title', 'description', 'category', 'created_at', 'price', 'image']
    readonly_fields = ['id', 'created_at']


admin.site.register(Products, ProductsAdmin)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'description']
    list_filter = ['id', 'category', 'description']
    search_fields = ['category']
    fields = ['id', 'category', 'description']
    readonly_fields = ['id']


admin.site.register(Categories, CategoriesAdmin)

