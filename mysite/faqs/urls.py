from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from faqs.views import FaqList

app_name = 'faqs'

urlpatterns = [
    path('', FaqList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)