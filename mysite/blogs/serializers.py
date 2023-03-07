from rest_framework import serializers
from blogs.models import Blog
from mysite.serializers import UserRelationModelSerializer

class BlogModelSerializer(serializers.ModelSerializer):
    author = UserRelationModelSerializer()
    class Meta:
        model = Blog
        exclude = ['id', 'is_draft']

class RelatedBlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'publish_on']