from django.db import models

# Create your models here.
class BlogpostModel:
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)