from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from events.views import EventDetail, EventList

app_name = 'events'

urlpatterns = [
    path('', EventList.as_view()),
    path('<slug:slug>/', EventDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)