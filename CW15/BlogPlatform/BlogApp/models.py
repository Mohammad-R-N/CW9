from django.db import models
from dataclasses import dataclass

# Create your models here.
@dataclass
class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=500)
    publication_date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

@dataclass
class Comment(models.Model):
    post=models.OneToOneField(Post,on_delete=models.CASCADE,primary_key=True)
    content=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    auther=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.auther
