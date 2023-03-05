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

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('knowledge-desk/', include(blogs_url)),
    path('expert-tips/', include(expert_tips_url)),
    path('events/', include(events_url)),
    path('testimonials/', include(testimonials_url)),
    path('faqs/', include(faqs_url)),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
