from django.db import models
from datetime import date #date module
from django.urls import reverse
from mysite.models import TimestampInfo, PostType
from django.contrib.auth.models import User #user model
from ckeditor_uploader.fields import RichTextUploadingField
from mysite.signals import brief_description_pre_save
from django.db.models.signals import pre_save


# Create your models here.
class ExpertTip(TimestampInfo): #extends timestamp info abstract class
    title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=350, unique=True, blank=True)
    detail = RichTextUploadingField(config_name='without_image')
    brief_description = models.TextField(blank=True, null=True)
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
    
pre_save.connect(brief_description_pre_save, sender=ExpertTip)