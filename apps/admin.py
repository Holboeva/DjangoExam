from django.contrib import admin

from apps.models import ProductImage, Product, Category
#
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    model = ProductImage
    max_num = 1
    min_num = 1
#
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product

#

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category


