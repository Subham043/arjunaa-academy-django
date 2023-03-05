from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from blogs.views import BlogDetail, BlogList

app_name = 'blogs'

urlpatterns = [
    path('', BlogList.as_view()),
    path('<slug:slug>/', BlogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)