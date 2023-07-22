from django.db import models

# Create your models here.


class Prompts(models.Model):
    pathway = models.CharField(max_length=255)
