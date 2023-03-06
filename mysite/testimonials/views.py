from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from testimonials.serializers import TestimonialModelSerializer
from testimonials.models import Testimonial


# Create your views here.
class TestimonialList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Testimonial.objects.without_draft()
    serializer_class = TestimonialModelSerializer