from django.db import models
from datetime import date, datetime #date module
from django.urls import reverse
from mysite.models import TimestampInfo
from courses.models import Course
from django.contrib.auth.models import User #user model
from django.utils.translation import gettext_lazy as _ #for post type

# Create your models here.

#request type choices
class RequestType(models.TextChoices): #creation choices for select field
    CALL_BACK = 'CALL_BACK', _('Call Back')
    HOME_VISIT = 'HOME_VISIT', _('Home Visit')
    VISIT_OUR_CENTER = 'VISIT_OUR_CENTER', _('Visit Our Center')
    CONNECT_ONLINE = 'CONNECT_ONLINE', _('Connect Online')

#branch type choices
class BranchType(models.TextChoices): #creation choices for select field
    VIJAYNAGAR = 'VIJAYNAGAR', _('Vijaynagar')
    HEBBAL = 'HEBBAL', _('Hebbal')
    KANAKAPURA_ROAD = 'KANAKAPURA_ROAD', _('Kanakapura Road')

#enquiry model
class Enquiry(TimestampInfo): #extends timestamp info abstract class
    name = models.CharField(max_length=350)
    email = models.EmailField()
    phone = models.PositiveBigIntegerField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name="enquiries_courses") #using the user model here for author forign key
    location = models.TextField()
    request = models.CharField(max_length=50, choices=RequestType.choices, default=RequestType.CALL_BACK) #using the choices for the charfield
    date = models.DateField(default=date.today) #using the date module here for default
    time = models.TimeField(default=datetime.now()) #using the date module here for default
    branch = models.CharField(max_length=50, choices=BranchType.choices, blank=True, null=True) #using the choices for the charfield
    detail = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="enquiries") #using the user model here for author forign key

    def __str__(self):
        return self.name