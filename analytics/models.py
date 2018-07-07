from django.db import models
from shorter.models import CutURL


class ClickEventManager(models.Manager):
    def create_event(self, CutIinstance):
        if isinstance( CutIinstance, CutURL):
            obj, created = self.get_or_create(cut_url=CutIinstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    cut_url = models.OneToOneField(CutURL)
    count = models.IntegerField(default=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = ClickEventManager()
    def __str__(self):
        return "{i}".format(i=self.count)