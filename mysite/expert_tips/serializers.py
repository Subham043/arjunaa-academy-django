from rest_framework import serializers
from expert_tips.models import ExpertTip
from mysite.serializers import UserBasicDetailSerializer

#exper tip full detail serializer
class ExpertTipModelSerializer(serializers.ModelSerializer):
    author = UserBasicDetailSerializer()
    class Meta:
        model = ExpertTip
        exclude = ['id', 'is_draft']

#expert tip basic detail serializer
class ExpertTipBasicDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertTip
        fields = ['title', 'slug', 'publish_on']