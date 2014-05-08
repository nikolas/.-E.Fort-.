from django.db import models

class SidebarItem(models.Model):
    content = models.CharField(max_length=200)
    position = models.IntegerField(default=0, unique=True)

    def __unicode__(self):
        return self.content


class Thumper(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(blank=True, max_length=200)
    content = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to='images')
    votes = models.IntegerField(default=0)
    parent = models.IntegerField(null=True)

    def __unicode__(self):
        return self.content

    def is_valid(self):
        return not (not self.content and not self.image)
