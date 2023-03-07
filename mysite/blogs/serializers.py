from rest_framework import serializers
from blogs.models import Blog
from mysite.serializers import UserBasicDetailSerializer

#Blog full detail serializer
class BlogModelSerializer(serializers.ModelSerializer):
    author = UserBasicDetailSerializer()
    class Meta:
        model = Blog
        exclude = ['id', 'is_draft']

#Blog basic detail serializer
class BlogBasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'publish_on']