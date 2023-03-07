from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from events.serializers import EventModelSerializer, RelatedEventModelSerializer
from events.models import Event
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class EventList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Event.objects.published()
    serializer_class = EventModelSerializer

class EventDetail(APIView):
    """
    Retrieve, update or delete a article instance.
    """
    def get(self, request, slug, format=None):
        try:
            event = Event.objects.published().get(slug=slug)
            event_serializer = EventModelSerializer(event)
        except Event.DoesNotExist:
            raise Http404
        
        next_event = Event.objects.next_event(event.id)
        next_event_serializer = RelatedEventModelSerializer(next_event)

        prev_event = Event.objects.prev_event(event.id)
        prev_event_serializer = RelatedEventModelSerializer(prev_event)

        return Response({
            "expert_event":event_serializer.data,
            "prev_expert_event":prev_event_serializer.data,
            "next_expert_event":next_event_serializer.data,
        })