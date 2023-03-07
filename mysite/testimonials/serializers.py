from rest_framework import serializers
from testimonials.models import Testimonial

#testimonial serializer
class TestimonialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        exclude = ['id', 'is_draft', 'uploaded_by']