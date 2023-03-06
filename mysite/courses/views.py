from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from courses.serializers import CategoryModelSerializer, CourseModelSerializer
from courses.models import Category, Course


# Create your views here.
class CategoryList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Category.objects.without_draft()
    serializer_class = CategoryModelSerializer


class CourseDetail(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Course.objects.published()
    serializer_class = CourseModelSerializer