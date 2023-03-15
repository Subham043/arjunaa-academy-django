from rest_framework import generics
from courses.serializers import CourseModelSerializer, CategoryWithCourseSerializer, CourseBasicDetailSerializer, CategoryModelSerializer, CourseWithoutCategoryModelSerializer
from courses.models import Category, Course
from django.db.models import Prefetch
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.pagination import LimitOffsetPagination


# Create your views here.

#category list for nav bar
class CategoryListForNavBar(APIView):
    """
    Retrieve, update or delete a article instance.
    """
    def get(self, request, format=None):
        category_with_courses = Category.objects.prefetch_related(Prefetch('courses', queryset=Course.objects.published()))
        category_with_courses_serializer = CategoryWithCourseSerializer(category_with_courses, many=True)
        
        courses_without_category = Course.objects.published().filter(category__isnull=True)
        courses_without_category_serializer = CourseBasicDetailSerializer(courses_without_category, many=True)
        
        return Response({
            "category_with_courses":category_with_courses_serializer.data,
            "courses_without_category":courses_without_category_serializer.data,
        })


#category detail based on category slug
class CategoryDetail(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Category.objects.without_draft()
    serializer_class = CategoryModelSerializer

#courses list based on category slug
class CoursesListBasedOnCategorySlug(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    lookup_url_kwarg = 'slug'
    queryset = Course.objects.published()
    serializer_class = CourseWithoutCategoryModelSerializer
    

    def get_queryset(self, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            category = Category.objects.without_draft().get(slug=slug)
        except Category.DoesNotExist:
            raise Http404
        return super().get_queryset().filter(category=category.id)

#course detail based on course slug
class CourseDetail(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Course.objects.published()
    serializer_class = CourseModelSerializer