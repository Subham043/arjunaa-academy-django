from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from blogs.serializers import BlogModelSerializer
from blogs.models import Blog


# Create your views here.
class BlogList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Blog.objects.published()
    serializer_class = BlogModelSerializer


class BlogDetail(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Blog.objects.published()
    serializer_class = BlogModelSerializer