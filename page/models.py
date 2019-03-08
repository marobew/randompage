from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    count = models.IntegerField()