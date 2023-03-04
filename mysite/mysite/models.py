from django.db import models
from django.utils.translation import gettext_lazy as _ #for post type

# Create your models here.
class PostType(models.TextChoices): #creation choices for select field
    FOR_KIDS = 'FOR_KIDS', _('Kids')
    FOR_ADULTS = 'FOR_ADULTS', _('Adults')

class Rating(models.TextChoices): #creation choices for select field
    ONE_STAR = 1, _('One Star')
    TWO_STARS = 2, _('Two Stars')
    THREE_STARS = 3, _('Three Stars')
    FOUR_STARS = 4, _('Four Stars')
    FIVE_STARS = 5, _('Five Stars')

class TimestampInfo(models.Model): #abstract class for timestamp
    created_at = models.DateTimeField(auto_now_add=True) #only on creation datetime is added
    updated_at = models.DateTimeField(auto_now=True) #on every modification datetime is added

    class Meta:
        abstract = True #declares the current class as abstract
