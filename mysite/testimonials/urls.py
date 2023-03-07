from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from testimonials.views import TestimonialList

app_name = 'testimonials'

urlpatterns = [
    path('', TestimonialList.as_view()), #url for testimmonial list
]

urlpatterns = format_suffix_patterns(urlpatterns)