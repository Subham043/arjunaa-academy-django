from rest_framework import serializers
from courses.models import Category, Course

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id', 'is_draft', 'uploaded_by']

class CourseModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    class Meta:
        model = Course
        exclude = ['id', 'is_draft', 'uploaded_by']

class CourseWithoutCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['id', 'is_draft', 'uploaded_by']

class RelatedCourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'slug']

class CategoryWithCourseSerializer(serializers.ModelSerializer):
    courses_category = RelatedCourseModelSerializer(many=True)
    class Meta:
        model = Category
        fields = ['title', 'slug', 'courses_category']
