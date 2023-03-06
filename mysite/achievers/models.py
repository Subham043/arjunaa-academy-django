from django.db import models
from datetime import date #date module
from django.urls import reverse
from mysite.models import TimestampInfo, CommonManager
from django.contrib.auth.models import User #user model

# Create your models here.
class Category(TimestampInfo): #extends timestamp info abstract class
    title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=350, unique=True, blank=True)
    detail = models.TextField(blank=True, null=True)
    is_draft = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user_category") #using the user model here for author forign key
    meta_title = models.TextField(blank=True, null=True)
    og_title = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)

    objects = CommonManager()

    def __str__(self):
        return self.title
    
class Result(TimestampInfo): #extends timestamp info abstract class
    student_name = models.CharField(max_length=350)
    student_rank = models.CharField(max_length=350, blank=True, null=True)
    college_name = models.CharField(max_length=350, blank=True, null=True)
    image = models.ImageField(upload_to='achievers/%Y/%m/%d/')# file will be saved to MEDIA_ROOT/uploads/2015/01/30
    is_draft = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user_result") #using the user model here for author forign key
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="achievers_category") #using the user model here for author forign key

    objects = CommonManager()

    def __str__(self):
        return self.student_name
    