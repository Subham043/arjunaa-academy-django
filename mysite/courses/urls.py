from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from courses.views import CourseDetail, CategoryListForNavBar, CategoryDetail, CoursesListBasedOnCategorySlug

app_name = 'courses'

urlpatterns = [
    path('category/', CategoryListForNavBar.as_view()), #url for courses category list
    path('category/<slug:slug>/', CategoryDetail.as_view()), #url for courses category detail
    path('category/<slug:slug>/list', CoursesListBasedOnCategorySlug.as_view()), #url for courses list based on category slug
    path('<slug:slug>/', CourseDetail.as_view()), #url for course detail based on course slug
]

urlpatterns = format_suffix_patterns(urlpatterns)