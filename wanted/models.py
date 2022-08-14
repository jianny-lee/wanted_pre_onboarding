from django.db import models

# Create your models here.
class Company(models.Model):
    position = models.CharField(max_length=200)
    money = models.IntegerField(default=0)
    detail = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)

    def __str__(self):return self.position