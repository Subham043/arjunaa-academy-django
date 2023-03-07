from rest_framework import serializers
from events.models import Event

class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['id', 'is_draft', 'uploaded_by']


class RelatedEventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_title', 'slug', 'publish_on']