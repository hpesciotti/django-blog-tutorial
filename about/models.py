from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class About(models.Model):
    
    title = models.CharField(max_length=30, unique=True)
    content = models.TextField()
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} | written by {self.update_on}"