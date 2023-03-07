from rest_framework import serializers
from achievers.models import Category, Result

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id', 'is_draft', 'uploaded_by']

class ResultModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        exclude = ['id', 'is_draft', 'uploaded_by', 'category']