from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Story(models.Model):
    user = models.ForeignKey(User)
    context = models.CharField(max_length=500,blank=False,null=False)
    passed = models.BooleanField(default=False)
    checked = models.BooleanField(default=False)
    published_date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.context

class Comment(models.Model):
    user = models.ForeignKey(User)
    story = models.ForeignKey(Story)
    comment = models.CharField(max_length=100,blank=False,null=False)
    comment_date = models.DateTimeField(default=timezone.now)

    def story_id(self):
        return story__pk

    def __unicode__(self):
        return self.comment