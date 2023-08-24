from django.contrib import admin
from django.http import request
from .models import Contact, Customer, Product
from django.utils.html import format_html
from django.urls import reverse
from import_export.admin import ImportExportModelAdmin


admin.site.site_header = 'Brandz City'


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'phone_number',
                    'house_number', 'locality', 'landmark', 'city']


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'title', 'description',
                    'original_price', 'price', 'category', 'product_img']

    def customer_info(self, obj):
        link = reverse("admin:app_customer_change",
                       args=[obj.customer.pk])
        return format_html("<a href='{}'>{}</a>", link, obj.customer.name)




@admin.register(Contact)
class ContactModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'contact_for', 'text']
