from django.db import models
from datetime import date, datetime #date module
from django.urls import reverse
from mysite.models import TimestampInfo, PostType
from django.contrib.auth.models import User #user model
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Event(TimestampInfo): #extends timestamp info abstract class
    event_title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=350, unique=True, blank=True)
    event_detail = RichTextUploadingField()
    event_for = models.CharField(max_length=50, choices=PostType.choices, default=PostType.FOR_ADULTS) #using the choices for the charfield
    event_banner = models.ImageField(upload_to='events/%Y/%m/%d/')# file will be saved to MEDIA_ROOT/uploads/2015/01/30
    event_location = models.CharField(max_length=350)
    phone = models.CharField(max_length=350)
    event_website = models.CharField(max_length=350)
    event_organizer = models.CharField(max_length=350)
    event_date = models.DateField(default=date.today, blank=True) #using the date module here for default
    event_time = models.TimeField(default=datetime.now(), blank=True) #using the date module here for default
    publish_on = models.DateField(default=date.today, blank=True) #using the date module here for default
    is_draft = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="events") #using the user model here for author forign key
    meta_title = models.TextField(blank=True, null=True)
    og_title = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.event_title