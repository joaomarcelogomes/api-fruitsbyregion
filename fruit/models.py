from django.db import models
from region.models import Region

class Fruit(models.Model):
    name = models.CharField(max_length=150, primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name