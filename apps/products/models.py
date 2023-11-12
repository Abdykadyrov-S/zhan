from django.db import models

from apps.users.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Категории"

class Shop(models.Model):
    name = models.CharField(max_length=100)
    url = models.SlugField()
    logo = models.ImageField(upload_to='shop_logo')
    banner = models.ImageField(upload_to='shop_banner')
    domain = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='shop_category')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории Магазина"
class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(blank=True, null=True
    )
    image = models.ImageField(upload_to="products_image")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products_shop')
    created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_products')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Продукты"

class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_review")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_review")
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name_plural = "Отзывы"



