from rest_framework import serializers
from courses.models import Category, Course

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id', 'is_draft', 'uploaded_by']

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['id', 'is_draft', 'uploaded_by']