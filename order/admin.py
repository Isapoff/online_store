from django.contrib import admin

from .models import Order, OrderItem


class OrderItemsInline(admin.TabularInline):
    model = Order.items.through
    fields = ['products', 'quantity', 'price']
    readonly_fields = ['products', 'quantity', 'price']
    extra = 0

    def products(self, instacne):
        return instacne.orderitems
    

    def quantity(self, instacne):
        return instacne.orderitems.quantity

    
    def price(self, instacne):
        return instacne.orderitems.price


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]
    exclude = ['items']
    list_display = (
        'id', 'user', 'status', 'created_at', 'total'
    )


admin.site.register(Order, OrderAdmin)

