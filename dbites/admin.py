from django.contrib import admin

from .models import Customer


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_name', 'email', 'phone_number')
    list_filter = ('cust_name', 'email')
    search_fields = ('cust_name',)
    ordering = ['cust_name']


admin.site.register(Customer)




