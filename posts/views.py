from posts.serializers import Postserializer
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from rest_framework import permissions

from .models import Post


class PostList(ListCreateAPIView):
    # bu ruhsatnoma faqat login qilganlar gina kurishi va uzgartirishi mumkin Loyiha darajasidagi ruxsatnomni sttingga kirib beramiz AlloAny urniga
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = Postserializer
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = Postserializer
    