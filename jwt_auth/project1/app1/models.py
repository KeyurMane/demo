from django.db import models

# Create your models here.
class Products(models.Model):
    pname = models.CharField(max_length=20)
    price = models.FloatField()
    pqty = models.IntegerField()

    def __str__(self):
        return self.pname