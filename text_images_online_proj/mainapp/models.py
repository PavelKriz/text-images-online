from django.db import models
from .default_images import IMAGE_PIN

# Create your models here.

class ImageModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    text_image = models.TextField(default=IMAGE_PIN) 
    def __str__(self):
        return self.title
    class Meta:
        db_table = "image"