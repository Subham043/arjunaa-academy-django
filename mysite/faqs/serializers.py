from rest_framework import serializers
from faqs.models import Faq

class FaqModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'