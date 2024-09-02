from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
