from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from books import serializer
from books.models import Book
from books.serializer import BookSerializer


@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)  # Serializer nesnesi burada oluşturuluyor
    return Response(serializer.data)  

@api_view(['GET'])
def book(request, id):
    try:
        book = Book.objects.get(pk = id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except:
        return Response({"error": "Eşleşen kayıt bulunamadı."} , status = status.HTTP_404_NOT_FOUND)

@api_view(["PUT"])
def book_update(request , id):
    book = Book.objects.get(pk = id)
    serializer = BookSerializer(book , data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view((["DELETE"]))
def book_delete(request , id):
    book = Book.objects.get(pk = id)
    book.delete()
    return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def book_create(request):
    serializer = BookSerializer(data = request.data)
    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
