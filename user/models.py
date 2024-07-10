from django.db import models
from datetime import datetime
from django.urls import reverse 

class User(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)

    def get_absolute_url(self):
        return reverse("usuarios", args=[str(self.id)])

    def __str__(self):
        return self.name