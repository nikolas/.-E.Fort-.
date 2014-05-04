from django.db import models

class Spool(models.Model):
    subject = models.CharField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.subject


class Thumper(models.Model):
    spool = models.ForeignKey(Spool)
    created_at = models.DateTimeField(auto_now_add=True)
    author_text = models.CharField(blank=True, max_length=200)
    content_text = models.CharField(blank=True, max_length=2000)
    image = models.ImageField(blank=True, upload_to='images')
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.content_text
