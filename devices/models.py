from django.db import models
from accounts.models import Family

class ChildDevice(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='devices')
    device_name = models.CharField(max_length=255)
    device_identifier = models.CharField(max_length=255, unique=True)
    operating_system = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='offline')
    last_seen = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
