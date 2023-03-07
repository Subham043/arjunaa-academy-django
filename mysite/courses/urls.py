from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from courses.views import CourseDetail, CategoryListForNavBar, CategoryDetail, CoursesListBasedOnCategorySlug

app_name = 'courses'

urlpatterns = [
    path('category/', CategoryListForNavBar.as_view()),
    path('category/<slug:slug>/', CategoryDetail.as_view()),
    path('category/<slug:slug>/list', CoursesListBasedOnCategorySlug.as_view()),
    path('<slug:slug>/', CourseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)