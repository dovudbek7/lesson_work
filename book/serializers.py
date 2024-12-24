from rest_framework import serializers
from .models import Author, Book, Order, OrderItem
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date', 'biography']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'price', 'stock']


class OrderItemSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'book', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    books = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'books', 'created_at', 'total_price']
