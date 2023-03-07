from rest_framework import serializers
from django.contrib.auth.models import User

#user basic detail serializers
class UserBasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']