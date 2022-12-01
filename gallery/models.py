from django.db import models


# Create your models here.
class Gallery_Model(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    contents = models.TextField()

    def __str__(self):
        return self.title
