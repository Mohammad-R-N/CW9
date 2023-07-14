from django.db import models
from dataclasses import dataclass


@dataclass
class Author(models.Model):
    name=models.CharField(max_length=50)
    bio=models.TextField()

    def __str__(self) -> str:
        return self.name