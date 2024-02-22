from django.db import models


class MyModel(models.Model):
    path = models.CharField(max_length=100)
