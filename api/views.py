from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from Goods.models import Product, Category
from .serializer import ProductSerializer, CategorySerializer, UserSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'user': UserSerializer(user).data,
            'message': 'Ro\'yxatdan muvaffaqiyatli o\'tdingiz'
        }, status=status.HTTP_201_CREATED)
    return Response({
        'errors': serializer.errors,
        'message': 'Ro\'yxatdan o\'tishda xatolik'
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            'token': token.key,
            'message': 'Tizimga muvaffaqiyatli kirdingiz'
        }, status=status.HTTP_200_OK)
    
    return Response({
        'error': 'Kirishda xatolik',
        'message': 'Foydalanuvchi nomi yoki parol noto\'g\'ri'
    }, status=status.HTTP_400_BAD_REQUEST)
