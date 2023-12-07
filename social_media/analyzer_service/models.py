from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    user_id = models.CharField(max_length=255)