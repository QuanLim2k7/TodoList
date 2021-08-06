from django.db import models
from django.db.models.base import Model

class Task(models.Model):
    title=models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(seft):
        return seft.title