from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=50,null=True)
    bio=models.TextField(null=True)
    
    def __str__(self) -> str:
        return self.name