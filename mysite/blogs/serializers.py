from rest_framework import serializers
from blogs.models import Blog

class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['id', 'is_draft']