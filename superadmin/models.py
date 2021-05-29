from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to='media/')
    
class Tags(models.Model):
    tag = models.CharField(max_length=20)
    weight = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
class PostDetails(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    description = models.TextField()
    