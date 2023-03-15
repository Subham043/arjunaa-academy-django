from rest_framework import serializers
from courses.models import Category, Course

#category full detail serializer
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id', 'is_draft', 'uploaded_by']

#course full detail serializer along with category full detail
class CourseModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    class Meta:
        model = Course
        exclude = ['id', 'is_draft', 'uploaded_by']

#course full detail serializer without category detail
class CourseWithoutCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ['id', 'is_draft', 'uploaded_by']

#course basic detail
class CourseBasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'slug']

#category basic detail along with course basic detail
class CategoryWithCourseSerializer(CategoryModelSerializer):
    courses = CourseBasicDetailSerializer(many=True)
    class Meta(CategoryModelSerializer.Meta):
        exclude = ['id', 'is_draft', 'uploaded_by', 'created_at', 'updated_at', 'detail', 'meta_title', 'og_title', 'meta_description', 'og_description']
