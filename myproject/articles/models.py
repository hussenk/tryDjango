from django.db import models

# Create your models here.

class Article(models.Model):
    content = models.TextField()
    title = models.TextField()
    def __str__(self):
        return self.title

    def __unicode__(self):
        return 

