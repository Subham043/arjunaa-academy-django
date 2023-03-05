from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from courses.views import CourseDetail, CategoryList

app_name = 'courses'

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('<slug:slug>/', CourseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)