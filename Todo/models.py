from pydoc import describe
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateTimeField
from sqlalchemy import true
from tables import Description

# Create your models here.


class task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
