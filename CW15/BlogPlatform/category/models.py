from django.db import models
from dataclasses import dataclass

# Create your models here.
@dataclass
class Category(models.Model):

    name=models.CharField(max_length=50)
    description=models.TextField()
    
    def __str__(self) -> str:
        return self.name