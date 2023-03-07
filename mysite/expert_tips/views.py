from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from expert_tips.serializers import ExpertTipModelSerializer, RelatedExpertTipModelSerializer
from expert_tips.models import ExpertTip
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class ExpertTipList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = ExpertTip.objects.published_with_author()
    serializer_class = ExpertTipModelSerializer

class ExpertTipDetail(APIView):
    """
    Retrieve, update or delete a article instance.
    """
    def get(self, request, slug, format=None):
        try:
            tip = ExpertTip.objects.published_with_author().get(slug=slug)
            tip_serializer = ExpertTipModelSerializer(tip)
        except ExpertTip.DoesNotExist:
            raise Http404
        
        next_tip = ExpertTip.objects.next_tip(tip.id)
        next_tip_serializer = RelatedExpertTipModelSerializer(next_tip)

        prev_tip = ExpertTip.objects.prev_tip(tip.id)
        prev_tip_serializer = RelatedExpertTipModelSerializer(prev_tip)

        return Response({
            "expert_tip":tip_serializer.data,
            "prev_expert_tip":prev_tip_serializer.data,
            "next_expert_tip":next_tip_serializer.data,
        })