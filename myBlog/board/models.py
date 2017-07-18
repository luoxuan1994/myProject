from django.db import models


class Message(models.Model):
    message_text = models.CharField(max_length=2000)
    message_name = models.CharField(max_length=20)
    support = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')