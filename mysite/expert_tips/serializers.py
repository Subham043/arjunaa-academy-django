from rest_framework import serializers
from expert_tips.models import ExpertTip

class ExpertTipModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertTip
        fields = '__all__'