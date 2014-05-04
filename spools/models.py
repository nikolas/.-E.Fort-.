from django.db import models

class Spool(models.Model):
    subject = models.CharField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.subject

    def is_valid(self):
        return (self.thumper_set.count() > 0) and \
            True in [_.is_valid() for _ in self.thumper_set.all()]


class SidebarItem(models.Model):
    content = models.CharField(max_length=200)
    position = models.IntegerField(default=0, unique=True)

    def __unicode__(self):
        return self.content


class Thumper(models.Model):
    spool = models.ForeignKey(Spool)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(blank=True, max_length=200)
    content = models.CharField(blank=True, max_length=2000)
    image = models.ImageField(blank=True, upload_to='images')
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.content

    def is_valid(self):
        return not (not self.content and not self.image)
