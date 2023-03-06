from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from events.serializers import EventModelSerializer
from events.models import Event


# Create your views here.
class EventList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Event.objects.published()
    serializer_class = EventModelSerializer


class EventDetail(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Event.objects.published()
    serializer_class = EventModelSerializer