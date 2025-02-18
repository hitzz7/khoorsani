

# Register your models here.
# admin.py
from django.contrib import admin
from .models import Category, Product, ProductImage,Order,StartaProject

# Define an inline class for ProjectImage
class ProductImageInline(admin.TabularInline):  # You can use StackedInline for a different layout
    model = ProductImage
    extra = 1  # Number of empty forms to display in the admin

# Customize the Project admin
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline] 
    # Include the ProjectImage inline in the Project admin


# Register your models
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order) 
admin.site.register(StartaProject)  

