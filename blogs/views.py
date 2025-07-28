from django.shortcuts import render
from rest_framework import status ,generics,viewsets
from rest_framework.generics import ListAPIView
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer,CommentSerializer
from app.paginations import CustomPagination  # 👈 Add this
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]

    


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


