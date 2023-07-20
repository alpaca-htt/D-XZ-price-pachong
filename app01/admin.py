from django.contrib import admin
from app01.models import Product_number, Duw_product_price, Xz_product_price

# Register your models here.
class Product_numberAdmin(admin.ModelAdmin):
    list_display = ('name', 'xl_number', 'duw_number', 'xz_number')

    '''每页10条'''
    list_per_page = 10


class Duw_product_priceAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'duw_price', 'create_time')

    '''每页10条'''
    list_per_page = 10


class Xz_product_priceAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'xz_price', 'create_time')

    '''每页10条'''
    list_per_page = 10


admin.site.register(Product_number,Product_numberAdmin)
admin.site.register(Duw_product_price,Duw_product_priceAdmin)
admin.site.register(Xz_product_price,Xz_product_priceAdmin)