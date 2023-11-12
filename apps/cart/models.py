from django.db import models

from apps.products.models import Products


# Create your models here.
class Cart(models.Model):
    session_key = models.CharField(max_length=40, unique=True, verbose_name="Ключ сессии")
    items = models.ManyToManyField(Products, through='CartItem', verbose_name="Товары")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания корзины")

    def __str__(self):
        return f"{self.session_key}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Корзина")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество товара")

    def __str__(self):
        return f"{self.cart}"

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"


class Wishlist(models.Model):
    session_key = models.CharField(max_length=40, unique=True, verbose_name="Ключ сессии")
    items = models.ManyToManyField(Products, through='WishlistItem', verbose_name="Избранные товары")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания избранного")

    def __str__(self):
        return f"{self.session_key}"

    class Meta:
        verbose_name = "Корзина избранных"
        verbose_name_plural = "Корзины избранных"


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE, verbose_name="Избранное")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество товара")

    def __str__(self):
        return f"{self.wishlist}"

    class Meta:
        verbose_name = "Товар в корзине избранных"
        verbose_name_plural = "Товары в корзине избранных"