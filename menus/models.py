from django.db import models

# Create your models here.
class Restaurant (models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return f"[Restaurant] name: {self.name}"
    
class MenuItem (models.Model):
    category = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=6)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"[MenuItem] description: {self.description[:50]}"