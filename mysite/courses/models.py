from django.db import models
from datetime import date #date module
from django.urls import reverse
from mysite.models import TimestampInfo
from django.contrib.auth.models import User #user model
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Category(TimestampInfo): #extends timestamp info abstract class
    title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=350, unique=True, blank=True)
    detail = models.TextField(blank=True, null=True)
    is_draft = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user_course_category") #using the user model here for author forign key
    meta_title = models.TextField(blank=True, null=True)
    og_title = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Course(TimestampInfo): #extends timestamp info abstract class
    title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=350, unique=True, blank=True)
    breif_description = models.TextField()
    detail = RichTextUploadingField()
    banner = models.ImageField(upload_to='courses/%Y/%m/%d/')# file will be saved to MEDIA_ROOT/uploads/2015/01/30
    actual_price = models.PositiveBigIntegerField()
    discount_in_percentage = models.PositiveBigIntegerField(blank=True, null=True)
    discounted_price = models.PositiveBigIntegerField(blank=True, null=True)
    publish_on = models.DateField(default=date.today, blank=True) #using the date module here for default
    is_draft = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses_category") #using the user model here for author forign key
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="courses") #using the user model here for author forign key
    meta_title = models.TextField(blank=True, null=True)
    og_title = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title