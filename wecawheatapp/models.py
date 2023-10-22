from django.db import models

# Create your models here.
class Item(models.Model):
    title1 = models.CharField(max_length=200, null = True)
    content_1 = models.ImageField( upload_to  = 'item_images/',null = True)
    description1 = models.TextField(null = True, blank = True)
    title2 = models.CharField(max_length=200, null = True)  
    content_2 = models.ImageField( upload_to  = 'item_images/', null = True)
    description2 = models.TextField(null = True, blank = True)
    title3 = models.CharField(max_length=200, null = True)
    content_3 = models.ImageField( upload_to  = 'item_images/', null = True)
    description3 = models.TextField(null = True, blank = True)
    title4 = models.CharField(max_length=200, null = True)
    content_4 = models.ImageField( upload_to  = 'item_images/', null = True)
    description4 = models.TextField(null = True, blank = True)
    title = models.CharField(max_length=200, null = True)
    content_image = models.ImageField( upload_to  = 'item_images/', null = True)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.title