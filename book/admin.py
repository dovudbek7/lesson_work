from django.contrib import admin
from .models import Author, Book, Order, OrderItem

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderItem)
