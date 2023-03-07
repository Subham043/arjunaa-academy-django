from rest_framework import serializers
from achievers.models import Category, Result

#achievers category serializer
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id', 'is_draft', 'uploaded_by']

#achievers result serializer
class ResultModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        exclude = ['id', 'is_draft', 'uploaded_by', 'category']