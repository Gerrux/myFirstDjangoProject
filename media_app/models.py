from django.db import models

# Create your models here.


class Media(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
