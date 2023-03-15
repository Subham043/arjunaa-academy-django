from django.db import models
from datetime import date #date module
from django.urls import reverse
from mysite.models import TimestampInfo, CommonManager
from django.contrib.auth.models import User #user model
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

#Leadership team Abstract Model inherited from timestamp abstract model
class LeadershipTeam(TimestampInfo):
    name = models.CharField(max_length=350)
    qualification = models.CharField(max_length=350, null=True, blank=True)
    designation = models.CharField(max_length=350)
    is_draft = models.BooleanField(default=False)

    objects = CommonManager()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True #declares the current class as abstract

#management model
class Management(LeadershipTeam): #extends timestamp info abstract class
    detail = RichTextUploadingField(config_name='without_image')
    image = models.ImageField(upload_to='management/%Y/%m/%d/')# file will be saved to MEDIA_ROOT/uploads/2015/01/30
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="managements_uploaded") #using the user model here for author forign key

#faculty model
class Faculty(LeadershipTeam): #extends timestamp info abstract class
    detail = models.TextField()
    image = models.ImageField(upload_to='faculty/%Y/%m/%d/')# file will be saved to MEDIA_ROOT/uploads/2015/01/30
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="faculties_uploaded") #using the user model here for author forign key
