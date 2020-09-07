from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone
import pytz


class FaqL(models.Model):
    question = models.CharField(max_length=256,blank=False) 
    answer = models.TextField(blank=True)
    date = models.DateTimeField(blank=True)
    author = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.question
    
    def date_pretty(self):
        return self.date.strftime("%b %e %Y ")

    
@receiver(signals.pre_save, sender=FaqL)
def set_date_time(sender, instance, **kwargs):
    if not instance.date:
        instance.date = timezone.now()  
