from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from leadership_teams.serializers import ManagementModelSerializer, FacultyModelSerializer
from leadership_teams.models import Management, Faculty


# Create your views here.
class ManagementList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Management.objects.without_draft()
    serializer_class = ManagementModelSerializer

class FacultyList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    default_limit = 12
    max_limit = 12
    queryset = Faculty.objects.without_draft()
    serializer_class = FacultyModelSerializer