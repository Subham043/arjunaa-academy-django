from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from achievers.serializers import CategoryModelSerializer, ResultModelSerializer
from achievers.models import Category, Result


# Create your views here.

#list for achievers category
class CategoryList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Category.objects.without_draft()
    serializer_class = CategoryModelSerializer

#list for achievers results
class ResultList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Result.objects.without_draft()
    serializer_class = ResultModelSerializer