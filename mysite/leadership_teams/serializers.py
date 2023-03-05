from rest_framework import serializers
from leadership_teams.models import Management, Faculty

class ManagementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'

class FacultyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'