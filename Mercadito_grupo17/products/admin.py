from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "price", "talle", "is_active", "created_at")
    list_filter = ("type", "is_active", "created_at", "talle")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}