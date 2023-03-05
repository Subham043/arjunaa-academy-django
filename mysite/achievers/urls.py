from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from achievers.views import CategoryList, ResultList

app_name = 'achievers'

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('<str:category>/', ResultList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)