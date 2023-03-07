from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from faqs.serializers import FaqModelSerializer
from faqs.models import Faq


# Create your views here.

#faq list
class FaqList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Faq.objects.without_draft()
    serializer_class = FaqModelSerializer