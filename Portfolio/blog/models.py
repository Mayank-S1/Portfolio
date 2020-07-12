from django.db import models

class Blog(models.Model):
      title = models.CharField(max_length=225)
      pub_date = models.DateTimeField()
      image = models.ImageField(upload_to='images/')
      body = models.TextField()

def __str__(self):
    return self.title

def summary(self):
    return self.body[:100]

