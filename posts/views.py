from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from posts.serializers import Postserializer

from .models import Post


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
    