from django.db import models

from appUser.models import CustomUser


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
    title = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
