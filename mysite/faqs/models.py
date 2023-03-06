from django.db import models
from mysite.models import TimestampInfo, CommonManager
from django.contrib.auth.models import User #user model
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Faq(TimestampInfo): #extends timestamp info abstract class
    question = models.CharField(max_length=350)
    answer = RichTextUploadingField(config_name='without_image')
    is_draft = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="faqs") #using the user model here for author forign key

    objects = CommonManager()

    def __str__(self):
        return self.question