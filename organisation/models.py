from django.db import models

from user.models import User


class Organisation(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
