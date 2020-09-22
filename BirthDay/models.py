from django.db import models

# Create your models here.
class Amna_Zafer(models.Model):
    Image = models.ImageField()
    Transparant_Imag  = models.ImageField()
    Catagory = models.CharField(max_length=50)
    Occasion = models.CharField(max_length=50)
    Discription = models.TextField()
    def __str__(self):
        return self.Catagory