from django.contrib import admin

from apps.products.models import *

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Shop)
admin.site.register(Review)
