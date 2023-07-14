from django.db import models
from Author.models import Author
from category.models import Category

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=500)
    publication_date=models.DateTimeField(auto_now_add=True)
    auther=models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post=models.OneToOneField(Post,on_delete=models.CASCADE,primary_key=True)
    content=models.CharField(max_length=500)
    date=models.DateTimeField(auto_now_add=True)
    auther=models.ForeignKey(Author,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.content
