from django.db import models
from typing import Optional

class Posts(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=80)
    content = models.CharField(max_length=5000)
    date = models.DateField(null=True, blank=True)
