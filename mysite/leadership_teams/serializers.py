from rest_framework import serializers
from leadership_teams.models import Management, Faculty

class ManagementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        exclude = ['id', 'is_draft', 'uploaded_by']

class FacultyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        exclude = ['id', 'is_draft', 'uploaded_by']