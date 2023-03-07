"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from blogs import urls as blogs_url
from expert_tips import urls as expert_tips_url
from events import urls as events_url
from testimonials import urls as testimonials_url
from faqs import urls as faqs_url
from achievers import urls as achievers_url
from leadership_teams import urls as leadership_teams_url
from courses import urls as courses_url

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')), #debug toolbar url
    path('ckeditor/', include('ckeditor_uploader.urls')), #ck-editor url
    path('knowledge-desk/', include(blogs_url)), #knowledge-desk-app url
    path('expert-tips/', include(expert_tips_url)), #expert-tips-app url
    path('events/', include(events_url)), #events-app url
    path('testimonials/', include(testimonials_url)), #testimonial-app url
    path('faqs/', include(faqs_url)), #faq-app url
    path('achievers/', include(achievers_url)), #achievers-app url
    path('leadership-teams/', include(leadership_teams_url)), #leadership-team-app url
    path('courses/', include(courses_url)), #courses-app url
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls), #admin url
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media url
