from django.db import models

# Create your Theme models here.
class Sitesettings(models.Model):
    banner=models.ImageField(upload_to='media/site/')
    caption=models.TextField()