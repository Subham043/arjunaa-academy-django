from django.db import models
from datetime import date #date module
from django.urls import reverse
from mysite.models import TimestampInfo, Rating, CommonManager
from django.contrib.auth.models import User #user model
from django.utils.translation import gettext_lazy as _ #for post type


#testimonial type choices
class TestimonialType(models.TextChoices): #creation choices for select field
    STUDENTS = 'STUDENTS', _('Students')
    PARENTS = 'PARENTS', _('Parents')
    TEACHERS = 'TEACHERS', _('Teachers')

#testimonial model
class Testimonial(TimestampInfo): #extends timestamp info abstract class
    category = models.CharField(max_length=50, choices=TestimonialType.choices, default=TestimonialType.STUDENTS) #using the choices for the charfield
    name = models.CharField(max_length=350)
    designation = models.CharField(max_length=350, blank=True, null=True)
    message = models.TextField()
    rating = models.CharField(max_length=50, choices=Rating.choices, default=Rating.FIVE_STARS) #using the choices for the charfield
    image = models.ImageField(upload_to='testimonial/%Y/%m/%d/')# file will be saved to MEDIA_ROOT/uploads/2015/01/30
    is_draft = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="testimonials") #using the user model here for author forign key

    objects = CommonManager()

    def __str__(self):
        return self.name