from rest_framework import serializers
from testimonials.models import Testimonial

class TestimonialModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'