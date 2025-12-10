from django.contrib import admin
from .models import *

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name' , 'slug','description','is_active')
    list_filter = ('is_active',)
    search_fields = ('name' , 'description')
    ordering = ('name',)
    readonly_fields = ('slug',)


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','slug','price')
    list_editable = ('price',)
    fieldsets = (
        (
            'NAME' , {
                'fields': ('category','slug')
            }
        ),
        (
            'price' , {
                'fields' : ('price',)
            }
        ),
    )