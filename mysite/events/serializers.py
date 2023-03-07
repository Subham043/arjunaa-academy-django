from rest_framework import serializers
from events.models import Event

#event full detail serializer
class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ['id', 'is_draft', 'uploaded_by']

#event basic detail serializer
class EventBasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_title', 'slug', 'publish_on']