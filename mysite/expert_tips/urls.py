from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from expert_tips.views import ExpertTipDetail, ExpertTipList

app_name = 'expert_tips'

urlpatterns = [
    path('', ExpertTipList.as_view()), #url for expert tips list
    path('<slug:slug>/', ExpertTipDetail.as_view()), #url for expert tips detail based on expert tip slug
]

urlpatterns = format_suffix_patterns(urlpatterns)