from django.contrib import admin

from apps.cart.models import Cart, CartItem, Wishlist, WishlistItem

# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'display_items', 'created')

    def display_items(self, obj):
        items = obj.items.all()  # Получаем все связанные товары
        item_names = ", ".join([item.title for item in items])  # Формируем список имен товаров
        return item_names
    display_items.short_description = 'Items'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'display_items', 'created')

    def display_items(self, obj):
        items = obj.items.all()  # Получаем все связанные товары
        item_names = ", ".join([item.title for item in items])  # Формируем список имен товаров
        return item_names
    display_items.short_description = 'Items'

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('wishlist', 'product', 'quantity')