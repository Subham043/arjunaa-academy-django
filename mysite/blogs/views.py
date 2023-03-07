from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from blogs.serializers import BlogModelSerializer, RelatedBlogModelSerializer
from blogs.models import Blog
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.functions import (ExtractDay, ExtractMonth, ExtractQuarter, ExtractWeek, ExtractIsoWeekDay, ExtractWeekDay, ExtractIsoYear, ExtractYear)
from django.db.models import F


# Create your views here.
class BlogList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Blog.objects.published_with_author()
    serializer_class = BlogModelSerializer

class BlogDetail(APIView):
    """
    Retrieve, update or delete a article instance.
    """
    def get(self, request, slug, format=None):
        try:
            blog = Blog.objects.published_with_author().get(slug=slug)
            blog_serializer = BlogModelSerializer(blog)
        except Blog.DoesNotExist:
            raise Http404
        
        next_blog = Blog.objects.next_blog(blog.id)
        next_blog_serializer = RelatedBlogModelSerializer(next_blog)

        prev_blog = Blog.objects.prev_blog(blog.id)
        prev_blog_serializer = RelatedBlogModelSerializer(prev_blog)
        
        return Response({
            "blog":blog_serializer.data,
            "prev_blog":prev_blog_serializer.data,
            "next_blog":next_blog_serializer.data,
        })