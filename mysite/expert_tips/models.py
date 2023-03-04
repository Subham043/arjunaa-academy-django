from django.db import models
from datetime import date #date module
from django.utils.translation import gettext_lazy as _ #for post type
from django.urls import reverse
from mysite.models import TimestampInfo, PostType
from django.contrib.auth.models import User #user model
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class ExpertTip(TimestampInfo): #extends timestamp info abstract class
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    detail = RichTextUploadingField(config_name='without_image')
    article_for = models.CharField(max_length=50, choices=PostType.choices, default=PostType.FOR_ADULTS) #using the choices for the charfield
    publish_on = models.DateField(default=date.today, blank=True) #using the date module here for default
    is_draft = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="expert_tips") #using the user model here for author forign key
    meta_title = models.TextField(blank=True, null=True)
    og_title = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title