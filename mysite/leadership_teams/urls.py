from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from leadership_teams.views import ManagementList, FacultyList

app_name = 'leadership_teams'

urlpatterns = [
    path('management/', ManagementList.as_view()),
    path('faculty/', FacultyList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)