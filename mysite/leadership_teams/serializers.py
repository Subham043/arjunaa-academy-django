from rest_framework import serializers
from leadership_teams.models import Management, Faculty

#management serializers
class ManagementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        exclude = ['id', 'is_draft', 'uploaded_by']

#faculty serializers
class FacultyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        exclude = ['id', 'is_draft', 'uploaded_by']