from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .models import *
from .serializers import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_book(request):
    book = Book.objects.get_or_create(
        authors = request.data['authors'],
        title = request.data['title'],
        image_link = request.data['image_link'],
    )
    profile = Profile.objects.get(id=request.data['user'])
    profile.profile_books.add(book[0])
    return Response()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    Review.objects.create(
        profile = Profile.objects.get(id=request.data['user']),
        book = Book.objects.get(id=request.data['book']),
        content = request.data['content'],
    )
    return Response()


@api_view(['POST'])
@permission_classes([])
def create_user(request):
    user = User.objects.create(
        username = request.data['username'],
    )
    user.set_password(request.data['password'])
    user.save()
    profile = Profile.objects.create(
        user = user,
        first_name = request.data['first_name'],
        last_name = request.data['last_name']
    )
    profile.save()
    profile_serialized = ProfileSerializer(profile)
    return Response(profile_serialized.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_books(request):
    books = Book.objects.filter(profiles = Profile.objects.get(id=request.data['user'])).order_by('-id')
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    profile = user.profile
    serializer = ProfileSerializer(profile, many=False)
    return Response(serializer.data)