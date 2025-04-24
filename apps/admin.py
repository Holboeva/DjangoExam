from django.contrib.admin import register, ModelAdmin, StackedInline
from django.db.models.functions.datetime import TruncBase

from apps.models import ProductImage, Product, Category


class ProductImageAdmin(StackedInline):
    model = ProductImage
    max_num = 1
    min_num = 1


@register(Product)
class ProductAdmin(ModelAdmin):
    inlines = ProductImageAdmin,


@register(Category)
class CategoryAdmin(ModelAdmin):
    pass