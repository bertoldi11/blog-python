from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.title