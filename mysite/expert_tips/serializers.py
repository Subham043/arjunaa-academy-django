from rest_framework import serializers
from expert_tips.models import ExpertTip
from mysite.serializers import UserRelationModelSerializer

class ExpertTipModelSerializer(serializers.ModelSerializer):
    author = UserRelationModelSerializer()
    class Meta:
        model = ExpertTip
        exclude = ['id', 'is_draft']


class RelatedExpertTipModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertTip
        fields = ['title', 'slug', 'publish_on']