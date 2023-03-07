from django.db import models
from django.utils.translation import gettext_lazy as _ #for post type
from datetime import datetime #date module

# Create your models here.

#post type choices
class PostType(models.TextChoices): #creation choices for select field
    FOR_KIDS = 'FOR_KIDS', _('Kids')
    FOR_ADULTS = 'FOR_ADULTS', _('Adults')

#rating choices
class Rating(models.TextChoices): #creation choices for select field
    ONE_STAR = 1, _('One Star')
    TWO_STARS = 2, _('Two Stars')
    THREE_STARS = 3, _('Three Stars')
    FOUR_STARS = 4, _('Four Stars')
    FIVE_STARS = 5, _('Five Stars')

#Common Query Set
class CommonQuerySet(models.QuerySet):
    #is not draft queryset
    def not_draft(self):
        return self.filter(is_draft=False)

    #is published queryset
    def is_published(self):
        today = datetime.today()
        return self.filter(publish_on__lte=today)
    
#Common Manager
class CommonManager(models.Manager):
    def get_queryset(self):
        return CommonQuerySet(self.model, using=self._db)

    #without draft manager
    def without_draft(self):
        return self.get_queryset().not_draft().order_by('-created_at')
    
    #publised manager
    def published(self):
        return self.get_queryset().not_draft().is_published().order_by('-publish_on')

#Timestamp Abstract Model
class TimestampInfo(models.Model): #abstract class for timestamp
    created_at = models.DateTimeField(auto_now_add=True) #only on creation datetime is added
    updated_at = models.DateTimeField(auto_now=True) #on every modification datetime is added

    class Meta:
        abstract = True #declares the current class as abstract
