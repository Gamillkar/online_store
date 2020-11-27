from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    list_display = ['user']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated','total_sum']
    list_filter = ['paid', 'created', 'updated',]
    list_editable = ('paid',)
    inlines = [OrderItemInline]
