from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=150, primary_key=True)

    def __str__(self):
        return self.name