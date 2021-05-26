from django.db import models

# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to='media/')
    
class PostDetails(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    description = models.TextField()
    