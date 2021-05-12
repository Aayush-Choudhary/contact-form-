from django.db import models
from datetime import datetime
# Create your models here.

class contact(models.Model):
    name = models.CharField(default="Fahad Shah", max_length=100)
    email = models.CharField(default="codinggod19@gmail.com", max_length=100)
    message = models.CharField(default="I want 9/11 2012", max_length=2000)
    dateTime = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.name