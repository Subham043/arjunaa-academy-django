from rest_framework import serializers
from achievers.models import Category, Result

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ResultModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'