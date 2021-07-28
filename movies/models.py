from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Moives(models.Model):

     title=models.CharField(max_length=64)
     film_star=models.CharField(max_length=64)
     director=models.CharField(max_length=64)
     description=models.TextField()
     pg=models.IntegerField()
     feedback=models.TextField()
     added_by=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

     def __str__(self) :
         return self.title