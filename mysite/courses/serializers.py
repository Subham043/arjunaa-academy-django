from rest_framework import serializers
from courses.models import Category, Course

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'