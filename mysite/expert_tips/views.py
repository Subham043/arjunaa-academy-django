from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from expert_tips.serializers import ExpertTipModelSerializer
from expert_tips.models import ExpertTip


# Create your views here.
class ExpertTipList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = ExpertTip.objects.all()
    serializer_class = ExpertTipModelSerializer


class ExpertTipDetail(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = ExpertTip.objects.all()
    serializer_class = ExpertTipModelSerializer