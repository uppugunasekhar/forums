from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    subject_title = models.CharField(max_length = 50)
    subject_desc = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('published date')
    sub_uid = models.ForeignKey(User, default = 000)
    def __str__(self):
        return self.subject_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pubme_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
  
class Comment(models.Model):
    subject = models.ForeignKey(Subject, default = 000)
    text = models.CharField(max_length = 1000)
    time = models.DateTimeField('commented time')
    user = models.ForeignKey(User, default = 000)
